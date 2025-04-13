<template>
  <base-table
    :data="tableData"
    :columns="tableColumns"
    thead-classes="text-primary"
  >
  </base-table>
</template>

<script>
import axios from 'axios';
import { BaseTable } from "@/components";

export default {
  components: {
    BaseTable,
  },
  data() {
    return {
      tableData: [], // Dados da tabela
      tableColumns: ["ID", "Consumo","hora"] // Definição das colunas
    };
  },
  mounted() {
    this.fetchTableData();
  },
  methods: {
    async fetchTableData() {
      try {
        // Fazendo a requisição para a API
        const response = await axios.get("http://localhost:8000/payload");
        
        // Atualizando os dados da tabela com a resposta da API
        this.tableData = response.data.payLoad.map(item => ({
          id: item.id,
          consumo: item.consumo,
          hora: item.hora,
        }));
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    }
  },
};
</script>

<style scoped>
/* Adicione seu estilo aqui */
</style>
