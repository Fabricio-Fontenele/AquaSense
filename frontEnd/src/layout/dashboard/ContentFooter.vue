<template>
  <footer class="footer aquasense-footer">
    <div class="container-fluid d-flex flex-column flex-md-row justify-content-between align-items-center py-2">
      <ul class="nav mb-2 mb-md-0">
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/Fabricio-Fontenele/AquaSense" target="_blank" rel="noopener">
            <span class="footer-logo">💧 AquaSense</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="mailto:contato@aquasense.com.br">
            Contato
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/Fabricio-Fontenele/AquaSense#equipe" target="_blank">
            Equipe
          </a>
        </li>
      </ul>
      <div class="copyright text-muted">
        © {{ year }} com <i class="tim-icons icon-heart-2 text-danger"></i> por AquaSense &mdash; Água + Inteligência
        <span class="d-none d-md-inline">| Todos os direitos reservados.</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
};
</script>

<style scoped>
.aquasense-footer {
  background: #f7fafd;
  border-top: 1px solid #e1ecf4;
  font-size: 1rem;
}

.footer-logo {
  font-weight: bold;
  color: #007bff;
  font-size: 1.1em;
  letter-spacing: 1px;
}

.nav-link {
  color: #657786;
  transition: color 0.15s;
}

.nav-link:hover {
  color: #007bff;
  text-decoration: underline;
}

.copyright {
  font-size: 0.95em;
  letter-spacing: 0.2px;
}

.icon-heart-2 {
  margin: 0 2px;
}

@media (max-width: 767px) {
  .container-fluid {
    text-align: center;
  }

  .copyright {
    margin-top: 0.7em;
    display: block;
  }
}
</style>