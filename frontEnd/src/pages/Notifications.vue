<template>
  <div class="row">
    <!-- Card: Alertas Inteligentes -->
    <div class="col-lg-6 col-md-12 mb-4">
      <card>
        <template #header>
          <h4>Alertas Inteligentes</h4>
        </template>
        <base-alert type="danger" dismissible with-icon>
          <span class="tim-icons icon-bell-55"></span>
          <span>
            <b>Vazamento detectado!</b><br>
            Consumo acima do normal nas últimas 2 horas.<br>
            <small>Verifique imediatamente seu sistema.</small>
          </span>
        </base-alert>
        <base-alert type="warning" dismissible with-icon>
          <span class="tim-icons icon-bell-55"></span>
          <span>
            <b>Pico de consumo</b><br>
            Seu uso entre 18h e 19h foi 45% superior à média.<br>
            <small>Acompanhe pelo dashboard.</small>
          </span>
        </base-alert>
        <base-alert type="info" dismissible with-icon>
          <span class="tim-icons icon-bell-55"></span>
          <span>
            <b>Novo sensor IoT conectado!</b><br>
            Dados em tempo real estão sendo recebidos.<br>
            <small>Última atualização: {{ lastUpdate }}</small>
          </span>
        </base-alert>
        <base-alert type="success" dismissible with-icon>
          <span class="tim-icons icon-bell-55"></span>
          <span>
            <b>Meta mensal atingida!</b><br>
            Parabéns, você economizou {{ economia }} litros neste mês.<br>
            <span class="badge badge-success">+{{ pontos }} pts</span>
          </span>
        </base-alert>
        <div class="d-flex justify-content-end mt-3">
          <button class="btn btn-primary" @click="notifyDynamic">
            Disparar alerta personalizado
          </button>
        </div>
      </card>
    </div>

    <!-- Card: Estados do Sistema -->
    <div class="col-lg-6 col-md-12 mb-4">
      <card>
        <template #header>
          <h4>Estados do Sistema</h4>
        </template>
        <base-alert type="primary" dismissible>
          <span>
            <b>Sistema operacional</b> <br>
            Todas as integrações funcionando normalmente.
          </span>
        </base-alert>
        <base-alert type="info" dismissible>
          <span>
            <b>Login realizado</b><br>
            Bem-vindo, {{ usuario }}!
          </span>
        </base-alert>
        <base-alert type="success" dismissible>
          <span>
            <b>Cadastro efetuado</b><br>
            Sua conta AquaSense foi criada com sucesso.
          </span>
        </base-alert>
        <base-alert type="warning" dismissible>
          <span>
            <b>Consumo elevado</b><br>
            Atenção ao uso nas próximas horas!
          </span>
        </base-alert>
        <base-alert type="danger" dismissible>
          <span>
            <b>Erro de comunicação</b><br>
            Não foi possível conectar ao servidor IoT.
          </span>
        </base-alert>
      </card>
    </div>
  </div>
</template>

<script>
import { BaseAlert } from "@/components";

export default {
  components: {
    BaseAlert,
  },
  data() {
    return {
      usuario: "João",
      economia: 320,
      pontos: 25,
      lastUpdate: "16/07/2025 01:10",
    };
  },
  methods: {
    notifyDynamic() {
      // Exemplo de notificação dinâmica
      this.$notify({
        icon: "tim-icons icon-bell-55",
        horizontalAlign: "right",
        verticalAlign: "top",
        type: "info",
        message: "Alerta personalizado disparado via IA ou integração IoT.",
        timeout: 4000,
      });
    },
  },
};
</script>

<style scoped>
.mb-4 {
  margin-bottom: 1.5rem;
}

.card {
  min-height: 100%;
}

.base-alert {
  margin-bottom: 1rem;
  font-size: 1rem;
}

.badge-success {
  background: #28a745;
  color: #fff;
  margin-left: 8px;
  font-size: 0.9em;
  border-radius: 10px;
  padding: 0.3em 0.7em;
}

.btn-primary {
  min-width: 200px;
}
</style>