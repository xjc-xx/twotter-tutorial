<!--
 * @Author: CC-TSR
 * @Date: 2021-01-07 16:35:37
 * @LastEditTime: 2021-01-07 18:56:34
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\views\CovidMap.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div>
    <Header />
    <div
      style="background-color: #42b983; width: 100%; height: 93vh; z-index: 0"
      v-loading="isLoading"
    >
      <!-- <div
        style="
          float: left;
          position: relative;
          top: 50px;
          left: 250px;
        "
        v-if="!isChina"
      >
        <el-button type="success" @click="getworld">刷新</el-button>
        <el-button type="info" @click="setEc(0)">现存确诊</el-button>
        <el-button type="info" @click="setEc(1)">总确诊</el-button>
        <el-button type="info" @click="setEc(2)">新增确诊</el-button>
        <el-button type="info" @click="setEcs(check)">中国</el-button>
      </div> -->
      <div style="float: left; position: relative; left: 30%">
        <h3>上次更新时间{{ lastTime }}</h3>
        <el-button type="success" @click="getSd">刷新</el-button>
        <el-button type="info" @click="setEcs(0)">现存确诊</el-button>
        <el-button type="info" @click="setEcs(1)">总确诊</el-button>
        <el-button type="info" @click="setEcs(2)">新增确诊</el-button>
        <el-button type="info" @click="setEc(check)">全球</el-button>
      </div>
      <div style="width: 100%; height: 93vh;" ref="chart"></div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/TheHeader";
import * as echarts from "echarts";
import china from "../assets/json/china.json";

export default {
  name: "echartest",
  components: { Header },
  data() {
    return {
      chinaTotal: 0,
      chinaAdd: 0,
      chinaNow: 0,
      datas: [],
      worldData: [],
      lastTime: "",
      check: 0,
      isLoading: false,
      isChina: false,
      worldNames: [],
      worldValue: [],
    };
  },
  mounted() {
    this.isLoading = true;
    this.getSd();
    this.setEcs(0);
  },
  methods: {
    test(content) {
      return this.$http.post(
        "http://api.aifanyi.net/google.php",
        `content=${content}&from=zh-CN&fromtxt=中文&to=英文&totxt=英语`
      );
    },
    getworld() {
      this.isLoading = true;
      this.$http
        .post(
          "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
        )
        .then((res) => {
          let data = res.data.data;
          let names = [];
          data.forEach((item) => {
            names.push(item.name);
          });
          this.worldData = data;
          this.test(names).then((res) => {
            console.log(res.data.dst);
            let ss = res.data.dst;
            console.log(ss);
            let namess = ('"' + ss.replace(/, /g, '","') + '"').split(",");
            this.worldNames = namess;

            this.setEc(this.check);
            this.isLoading = false;
          });
        });
    },
    getSd() {
      this.isLoading = true;
      this.$http.post(`/api/getDisease.html`).then((res) => {
        let data = JSON.parse(res.data.data);
        console.log(data);
        let dss = data.areaTree[0].children;
        this.datas = dss;
        this.chinaTotal = data.chinaTotal.confirm;
        this.chinaAdd = data.chinaAdd.confirm;
        this.chinaNow = data.chinaTotal.nowConfirm;
        this.lastTime = data.lastUpdateTime;
        this.isLoading = false;
      });
    },
    setEcs(check) {
      let min = 0;
      let max = 100;
      let title = " 地图"; //地图标题(总，现存，新增)
      let data = []; //疫情数据
      let names = []; //提取省级名字
      let values = []; //提取城市疫情数据
      this.check = check; //获取选择(总，现存，新增)
      if (check === 0) {
        title = "国内现存确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.total.confirm - item.total.dead - item.total.heal);
          data.push({ name: names[index], value: values[index] });
        });
        min = 0;
        max = 100;
      }
      if (check === 1) {
        title = "国内总确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.total.confirm);
          data.push({ name: names[index], value: values[index] });
        });
        min = 0;
        max = 3000;
      }
      if (check === 2) {
        title = "国内新增确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.today.confirm);
          data.push({ name: names[index], value: values[index] });
        });
        min = 0;
        max = 5;
      }
      echarts.registerMap("china", china);
      let myChart = echarts.init(this.$refs.chart);
      myChart.clear();
      let option = {
        title: {
          text: title,
          left: "center",
        },
        tooltip: {
          trigger: "item",
          showDelay: 0,
          transitionDuration: 0.2,
        }, //工具
        visualMap: {
          left: "right",
          min: min,
          max: max,
          inRange: {
            color: [
              "#f9f9fa",
              // "#bfbfc0",
              // "#74add1",
              // "#abd9e9",
              // "#e0f3f8",
              // "#ffffbf",
              "#fee090",
              "#fdae61",
              "#f46d43",
              "#d73027",
              "#a50026",
            ], //颜色梯度
          },
          text: ["High", "Low"], // 文本，默认为数值文本 见地图
          calculable: true,
        },
        toolbox: {
          show: true,
          //orient: 'vertical',
          left: "left",
          top: "top",
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {},
          }, //工具功能
        },
        series: [
          {
            name: "数据",
            type: "map",
            roam: true,
            map: "china", //地图
            emphasis: {
              label: {
                show: true,
              },
            },
            itemStyle: {
              normal: {
                label: {
                  show: true, //显示城市名
                },
              },
            },
            data: data,
          },
        ],
      };
      myChart.setOption(option); //绘图
      this.isChina = true; //控制地图选择是否显示
      myChart.on("click", function (params) {
        console.log(params);
      });
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
</style>