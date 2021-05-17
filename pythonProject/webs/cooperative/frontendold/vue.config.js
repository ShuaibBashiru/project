var link = "http://localhost:8000"


module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: link,
        pathRewrite: { "^/api/": "/api/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/auth": {
        target: link,
        pathRewrite: { "^/auth/": "/auth/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/posts": {
        target: link,
        pathRewrite: { "^/posts/": "/posts/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/update": {
        target: link,
        pathRewrite: { "^/update/": "/update/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/download": {
        target: link,
        pathRewrite: { "^/download/": "/download/" },
        changeOrigin: true,
        logLevel: "debug"
      }
    }
  }
};