<template>
  <div>
    <div class="row">
      <div class="col-12">
        <card type="chart">
          <template slot="header">
            <div class="row">
              <div class="col-6" :class="isRTL ? 'text-right' : 'text-left'">
                <h5 class="card-category">Consumo Previsto Aproximado R$ {{ this.calculaExpectativa() }}</h5>
                <h2 class="card-title">Diário</h2>
              </div>
              <div
                class="col-6 text-right"
                :class="isRTL ? 'text-right' : 'text-left'"
              >
                <h2 class="card-title">{{this.obterDataAtualFormatada()}} - {{ consumoTotal }}m³</h2>
              </div>
            </div>
          </template>
          <div class="chart-area">
            <line-chart
              ref="bigChart"
              chart-id="big-line-chart"
              :chart-data="bigLineChart.chartData"
              :gradient-colors="bigLineChart.gradientColors"
              :gradient-stops="bigLineChart.gradientStops"
              :extra-options="bigLineChart.extraOptions"
              :height="100"
            />
          </div>
        </card>
      </div>

      <div class="col-12">
        <card class="card" :header-classes="{ 'text-right': isRTL }">
          <h4 slot="header" class="card-title">Histórico de consumo</h4>
          <div class="table-responsive">
            <user-table></user-table>
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import * as chartConfigs from "@/components/Charts/config";
import TaskList from "./Dashboard/TaskList";
import UserTable from "./Dashboard/UserTable";
import config from "@/config";

export default {
  components: {
    LineChart,
    UserTable,
  },
  data() {
    return {
      consumoTotal: 0,
      bigLineChart: {
        allData: [
          [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100],
          [80, 120, 105, 110, 95, 105, 90, 100, 80, 95, 70, 120],
          [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130],
        ],
        activeIndex: 0,
        chartData: {
          datasets: [{}],
          labels: [
            "JAN",
            "FEB",
            "MAR",
            "APR",
            "MAY",
            "JUN",
            "JUL",
            "AUG",
            "SEP",
            "OCT",
            "NOV",
            "DEC",
          ],
        },
        extraOptions: chartConfigs.purpleChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
        categories: [],
      },
      purpleLineChart: {
        extraOptions: chartConfigs.purpleChartOptions,
        chartData: {
          labels: ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
          datasets: [
            {
              label: "Data",
              fill: true,
              borderColor: config.colors.primary,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.primary,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.primary,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 70, 80, 120, 80],
            },
          ],
        },
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.2, 0],
      },
      greenLineChart: {
        extraOptions: chartConfigs.greenChartOptions,
        chartData: {
          labels: ["JUL", "AUG", "SEP", "OCT", "NOV"],
          datasets: [
            {
              label: "My First dataset",
              fill: true,
              borderColor: config.colors.danger,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.danger,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.danger,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [90, 27, 60, 12, 80],
            },
          ],
        },
        gradientColors: [
          "rgba(66,134,121,0.15)",
          "rgba(66,134,121,0.0)",
          "rgba(66,134,121,0)",
        ],
        gradientStops: [1, 0.4, 0],
      },
      blueBarChart: {
        extraOptions: chartConfigs.barChartOptions,
        chartData: {
          labels: ["USA", "GER", "AUS", "UK", "RO", "BR"],
          datasets: [
            {
              label: "Countries",
              fill: true,
              borderColor: config.colors.info,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: [53, 20, 10, 80, 100, 45],
            },
          ],
        },
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
      },
    };
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    bigLineChartCategories() {
      return this.$t("dashboard.chartCategories");
    },
  },
  methods: {
    obterDataAtualFormatada() {
      const dataAtual = new Date();
      return dataAtual.toLocaleDateString('pt-BR');
    },
    async fetchConsumptionData() {
      try {
        const response = await fetch("http://localhost:8000/payload");
        const data = await response.json();

        if (data.payLoad && Array.isArray(data.payLoad)) {
          // Pega os últimos 20 registros
          const lastItems = data.payLoad.slice(-20);

          // Extrai hora e consumo
          const labels = lastItems.map((item) => item.hora.split("/")[0]);
          const consumos = lastItems.map((item) => item.consumo);

          const chartData = {
            labels,
            datasets: [
              {
                label: "Consumo (litros)",
                fill: true,
                borderColor: config.colors.primary,
                borderWidth: 2,
                pointBackgroundColor: config.colors.primary,
                pointBorderColor: "rgba(255,255,255,0)",
                pointHoverBackgroundColor: config.colors.primary,
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                data: consumos,
              },
            ],
          };

          // Atualiza o gráfico
          this.$refs.bigChart.updateGradients(chartData);
          this.bigLineChart.chartData = chartData;
        } else {
          console.error("Formato de dados inesperado", data);
        }
      } catch (error) {
        console.error("Erro ao buscar dados de consumo:", error);
      }
    },
    async fetchConsumptionTotalData() {
        try {
          const response = await fetch("http://localhost:8000/consumo_diario");
          const data = await response.json();

            this.consumoTotal = data.consumo_total.toFixed(2);
          
        } catch (error) {
          console.error("Erro ao buscar dados de consumo:", error);
        }
    },
    calculaExpectativa(){
      let valor = this.consumoTotal * 6.00
      return valor.toFixed(2)
    }
  },
  mounted() {
    this.i18n = this.$i18n;
    if (this.enableRTL) {
      this.i18n.locale = "ar";
      this.$rtl.enableRTL();
    }
    this.fetchConsumptionData(); // <-- Atualiza o gráfico com os dados reais
    this.fetchConsumptionTotalData()
  },
  beforeDestroy() {
    if (this.$rtl.isRTL) {
      this.i18n.locale = "en";
      this.$rtl.disableRTL();
    }
  },
};
</script>
<style></style>
