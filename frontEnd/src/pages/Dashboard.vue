
<template>
  <div>
    <div class="row">
      <!-- Card: Consumo Diário -->
      <div class="col-12">
        <card type="chart" class="dashboard-card">
          <template #header>
            <div class="row align-items-center">
              <div class="col-6 text-left">
                <h5 class="card-category mb-0 text-muted">
                  Previsão de custo este mês: <span class="font-weight-bold text-primary">R$ {{ expectativa }}</span>
                </h5>
                <h2 class="card-title mt-1">Consumo Diário</h2>
                <p class="card-text mt-2 mb-0">
                  <span class="badge badge-info px-2 py-1">Meta Mensal: {{ metaMensal }} m³</span>
                  <span v-if="consumoTotal > metaMensal" class="badge badge-danger ml-2 px-2 py-1">Limite
                    atingido!</span>
                  <span v-else class="badge badge-success ml-2 px-2 py-1">Dentro da meta</span>
                </p>
              </div>
              <div class="col-6 text-right">
                <h2 class="card-title">
                  {{ dataAtualFormatada }} <span class="mx-2">|</span> <span class="text-success">{{ consumoTotal }}
                    <small>m³</small></span>
                </h2>
                <div class="mt-2">
                  <span class="badge badge-secondary">Perfil: {{ perfil }}</span>
                </div>
              </div>
            </div>
          </template>
          <div class="chart-area mt-3">
            <line-chart ref="bigChart" chart-id="big-line-chart" :chart-data="bigLineChart.chartData"
              :gradient-colors="bigLineChart.gradientColors" :gradient-stops="bigLineChart.gradientStops"
              :extra-options="bigLineChart.extraOptions" :height="120" />
          </div>
        </card>
      </div>

      <!-- Card: Histórico de Consumo -->
      <div class="col-12 mt-4">
        <card>
          <template #header>
            <h4 class="card-title mb-0">Histórico</h4>
            <small class="text-muted">Veja os últimos registros e tendências</small>
          </template>
          <div class="table-responsive historico-scroll">
            <user-table />
          </div>
        </card>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/Charts/LineChart";
import UserTable from "./Dashboard/UserTable";
import * as chartConfigs from "@/components/Charts/config";
import config from "@/config";

export default {
  components: {
    LineChart,
    UserTable,
  },
  data() {
    return {
      consumoTotal: 0,
      expectativa: "0.00",
      dataAtualFormatada: "",
      metaMensal: 30, // exemplo, pode vir do backend ou do perfil do usuário
      perfil: "Residencial", // pode ser dinâmico: Residencial, Comercial, Público
      bigLineChart: {
        chartData: {
          labels: [],
          datasets: [],
        },
        extraOptions: chartConfigs.purpleChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
      },
    };
  },
  methods: {
    formatDataAtual() {
      const dataAtual = new Date();
      this.dataAtualFormatada = dataAtual.toLocaleDateString("pt-BR");
    },
    async fetchConsumptionData() {
      try {
        const response = await fetch("http://localhost:8000/payload");
        const data = await response.json();

        if (data.payLoad && Array.isArray(data.payLoad)) {
          const lastItems = data.payLoad.slice(-20);
          const labels = lastItems.map(item =>
            item.DateTime ? new Date(item.DateTime).toLocaleDateString("pt-BR") : ""
          );
          const consumos = lastItems.map(item => item.consumo);

          this.bigLineChart.chartData = {
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

          if (this.$refs.bigChart) {
            this.$refs.bigChart.updateGradients(this.bigLineChart.chartData);
          }
        }
      } catch (error) {
        console.error("Erro ao buscar dados de consumo:", error);
      }
    },
    async fetchConsumptionTotalData() {
      try {
        const response = await fetch("http://localhost:8000/consumo_diario");
        const data = await response.json();

        this.consumoTotal = data.consumo_total ? data.consumo_total.toFixed(2) : "0.00";
        this.expectativa = (parseFloat(this.consumoTotal) * 6.0).toFixed(2);
      } catch (error) {
        console.error("Erro ao buscar dados de consumo total:", error);
      }
    },
  },
  mounted() {
    this.formatDataAtual();
    this.fetchConsumptionData();
    this.fetchConsumptionTotalData();
  },
};
</script>

<style scoped>
.dashboard-card {
  border-left: 8px solid #007bff;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
}

.card-category {
  font-size: 1rem;
  color: #6c757d;
}

.badge {
  font-size: 0.95em;
}

.historico-scroll {
  max-height: 400px;
  overflow-y: auto;
}

@media (max-width: 767px) {
  .dashboard-card {
    border-left: none;
    border-top: 8px solid #007bff;
  }
}
</style>