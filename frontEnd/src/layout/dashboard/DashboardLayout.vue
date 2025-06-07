<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
        <sidebar-link
          to="/dashboard"
          :name="$t('GRÁFICO')"
          icon="tim-icons icon-chart-pie-36"
        />
        <sidebar-link
          to="/notifications"
          :name="$t('NOTIFICAÇÕES DE CONSUMO')"
          icon="tim-icons icon-bell-55"
        />
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar"> </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,
    ContentFooter,
    DashboardContent,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
