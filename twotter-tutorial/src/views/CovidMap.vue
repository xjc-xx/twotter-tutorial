<!--
 * @Author: CC-TSR
 * @Date: 2021-01-07 16:35:37
 * @LastEditTime: 2021-01-07 19:29:00
 * @LastEditors: xiejiancheng1999@qq.com
 * @Description: 
 * @FilePath: \twotter-tutorial\src\views\CovidMap.vue
 * @可以输入预定的版权声明、个性签名、空行等
-->
<template>
  <div>
    <Header />

  <div
      style="background-color: #42b983;width: 100%;height: 92.5vh;"
      v-loading="isLoading"
    >
      <div
        style="float: left;position: relative;top:50px;left: 250px;z-index: 5"
        v-if="!isChina"
      >
        <el-button type="success" @click="getworld">刷新</el-button>
        <el-button type="info" @click="setEc(0)">现存确诊</el-button>
        <el-button type="info" @click="setEc(1)">总确诊</el-button>
        <el-button type="info" @click="setEc(2)">新增确诊</el-button>
        <el-button type="info" @click="setEcs(check)">中国</el-button>
      </div>
      <div
        style="float: left;position: relative;left: 250px;z-index: 5"
        v-if="isChina"
      >
        <h3>上次更新时间{{ lastTime }}</h3>
        <el-button type="success" @click="getSd">刷新</el-button>
        <el-button type="info" @click="setEcs(0)">现存确诊</el-button>
        <el-button type="info" @click="setEcs(1)">总确诊</el-button>
        <el-button type="info" @click="setEcs(2)">新增确诊</el-button>
        <el-button type="info" @click="setEc(check)">全球</el-button>
      </div>
      <div style="width: 90vw;height: 80vh;" ref="chart"></div>
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
      isChina: true,
      worldNames: [],
      worldValue: [],
    };
  },
  mounted() {
    this.isLoading = true;
    this.getSd();
    this.setEcs(0);
    // this.getworld();
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
      let title = " 地图";
      let data = [];
      let names = [];
      let values = [];
      this.check = check;
      if (check === 0) {
        title = "国内现存确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.total.confirm - item.total.dead - item.total.heal);
          data.push({
            name: names[index],
            value: values[index],
          });
        });
        min = 0;
        max = 100;
      }
      if (check === 1) {
        title = "国内总确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.total.confirm);
          data.push({
            name: names[index],
            value: values[index],
          });
        });
        min = 0;
        max = 3000;
      }
      if (check === 2) {
        title = "国内新增确诊地图";
        this.datas.forEach((item, index) => {
          names.push(item.name);
          values.push(item.today.confirm);
          data.push({
            name: names[index],
            value: values[index],
          });
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
        },
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
            ],
          },
          text: ["High", "Low"], // 文本，默认为数值文本
          calculable: true,
        },
        toolbox: {
          show: true,
          //orient: 'vertical',
          left: "left",
          top: "top",
          feature: {
            dataView: {
              readOnly: false,
            },
            restore: {},
            saveAsImage: {},
          },
        },
        series: [
          {
            name: "数据",
            type: "map",
            roam: true,
            map: "china",
            emphasis: {
              label: {
                show: true,
              },
            },
            itemStyle: {
              normal: {
                label: {
                  show: true,
                },
              },
            },
            // 文本位置修正

            data: data,
          },
        ],
      };
      myChart.setOption(option);
      this.isChina = true;
      myChart.on("click", function (params) {
        console.log(params);
      });
    },
    // setEc(check) {
    //   let datas = [];
    //   let title = "";
    //   this.isChina = false;
    //   this.check = check;
    //   let min = 0;
    //   let max = 100;
    //   echarts.registerMap("world", world);
    //   let values = [];
    //   if (check === 0) {
    //     this.worldData.forEach((item, index) => {
    //       values.push(item.nowConfirm);
    //       let sss = this.worldNames[index];
    //       sss = sss.substring(1, sss.length - 1);
    //       if (sss === "USA") {
    //         sss = "United States";
    //       }
    //       datas.push({
    //         name: sss,
    //         value: values[index],
    //       });
    //     });
    //     datas.push({
    //       name: "China",
    //       value: this.chinaNow,
    //     });
    //     title = "世界疫情现存地图";
    //     min = 1000;
    //     max = 100000;
    //   }
    //   if (check === 1) {
    //     this.worldData.forEach((item, index) => {
    //       values.push(item.confirm);
    //       let sss = this.worldNames[index];
    //       sss = sss.substring(1, sss.length - 1);
    //       if (sss === "USA") {
    //         sss = "United States";
    //       }
    //       datas.push({
    //         name: sss,
    //         value: values[index],
    //       });
    //     });
    //     datas.push({
    //       name: "China",
    //       value: this.chinaTotal,
    //     });
    //     title = "世界疫情总确诊地图";
    //     min = 100000;
    //     max = 1000000;
    //   }
    //   if (check === 2) {
    //     this.worldData.forEach((item, index) => {
    //       values.push(item.confirmAdd);
    //       let sss = this.worldNames[index];
    //       sss = sss.substring(1, sss.length - 1);
    //       if (sss === "USA") {
    //         sss = "United States";
    //       }
    //       datas.push({
    //         name: sss,
    //         value: values[index],
    //       });
    //     });
    //     datas.push({
    //       name: "China",
    //       value: this.chinaAdd,
    //     });
    //     title = "世界疫情新增确诊地图";
    //     min = 10;
    //     max = 1000;
    //   }

    //   let myChart = echarts.init(this.$refs.chart);
    //   myChart.clear();
    //   let option = {
    //     title: {
    //       text: title,
    //       left: "center",
    //     },
    //     tooltip: {
    //       trigger: "item",
    //       showDelay: 0,
    //       transitionDuration: 0.2,
    //     },
    //     visualMap: {
    //       left: "right",
    //       min: min,
    //       max: max,
    //       inRange: {
    //         color: [
    //           "#f9f9fa",
    //           // "#bfbfc0",
    //           // "#74add1",
    //           // "#abd9e9",
    //           "#e0f3f8",
    //           "#ffffbf",
    //           "#fee090",
    //           "#fdae61",
    //           "#f46d43",
    //           "#d73027",
    //           "#a50026",
    //         ],
    //       },
    //       text: ["High", "Low"], // 文本，默认为数值文本
    //       calculable: true,
    //     },
    //     toolbox: {
    //       show: true,
    //       //orient: 'vertical',
    //       left: "left",
    //       top: "top",
    //       feature: {
    //         dataView: {
    //           readOnly: false,
    //         },
    //         restore: {},
    //         saveAsImage: {},
    //       },
    //     },
    //     series: [
    //       {
    //         name: "数据",
    //         type: "map",
    //         roam: true,
    //         map: "world",
    //         emphasis: {
    //           label: {
    //             show: true,
    //           },
    //         },
    //         itemStyle: {
    //           normal: {
    //             label: {
    //               show: false,
    //             },
    //           },
    //         },
    //         // 文本位置修正

    //         data: datas,
    //       },
    //     ],
    //   };
    //   myChart.setOption(option);
    //   let vm = this;
    //   myChart.on("click", function (params) {
    //     console.log(params);
    //     if (params.name === "China") {
    //       console.log(1111);
    //       vm.setEcs(vm.check);
    //     }
    //   });
    // },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
</style>