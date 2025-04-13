<template>
  <div class="row">
    <div class="col-md-6">
      <card>
        <h4 slot="header">Notificações</h4>
        <base-alert type="info">
          <span>This is a plain notification</span>
        </base-alert>
        <base-alert type="info" dismissible>
          <span>This is a plain notification</span>
        </base-alert>
        <base-alert type="info" dismissible with-icon>
          <span data-notify="icon" class="tim-icons icon-bell-55"></span>
          <span data-notify="message"
            >This is a notification with close button and icon.</span
          >
        </base-alert>
        <base-alert type="info" dismissible with-icon>
          <span data-notify="icon" class="tim-icons icon-bell-55"></span>
          <span data-notify="message"
            >This is a notification with close button and icon and have many
            lines. You can see that the icon and the close button are always
            vertically aligned. This is a beautiful notification. So you don't
            have to worry about the style.</span
          >
        </base-alert>
      </card>
    </div>
    <div class="col-md-6">
      <card>
        <h4 slot="header">Notifications states</h4>
        <base-alert type="primary" dismissible>
          <span
            ><b> Primary - </b> This is a regular notification made with
            ".alert-primary"</span
          >
        </base-alert>
        <base-alert type="info" dismissible>
          <span
            ><b> Info - </b> This is a regular notification made with
            ".alert-info"</span
          >
        </base-alert>
        <base-alert type="success" dismissible>
          <span
            ><b> Success - </b> This is a regular notification made with
            ".alert-success"</span
          >
        </base-alert>
        <base-alert type="warning" dismissible>
          <span
            ><b> Warning - </b> This is a regular notification made with
            ".alert-warning"</span
          >
        </base-alert>
        <base-alert type="danger" dismissible>
          <span
            ><b> Danger - </b> This is a regular notification made with
            ".alert-danger"</span
          >
        </base-alert>
      </card>
    </div>
  </div>
</template>
<script>
import NotificationTemplate from "./Notifications/NotificationTemplate";
import { BaseAlert } from "@/components";

export default {
  components: {
    BaseAlert,
  },
  data() {
    return {
      type: ["", "info", "success", "warning", "danger"],
      notifications: {
        topCenter: false,
      },
    };
  },
  methods: {
    notifyVue(verticalAlign, horizontalAlign) {
      const color = Math.floor(Math.random() * 4 + 1);
      this.$notify({
        component: NotificationTemplate,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color],
        timeout: 0,
      });
    },
  },
};
</script>
<style></style>
