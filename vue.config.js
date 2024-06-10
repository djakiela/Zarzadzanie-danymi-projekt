const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: false,
        onProxyReq: (proxyReq) => {
          proxyReq.setHeader("Access-Control-Allow-Credentials", "true");
        },
      },
    },
  },
});
