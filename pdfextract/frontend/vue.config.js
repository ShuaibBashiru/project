module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:8000",
        pathRewrite: { "^/api/": "/api/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/pdfjs": {
        target: "https://cdn.mozilla.net",
        pathRewrite: { "^/pdfjs/": "/pdfjs/" },
        changeOrigin: true,
        logLevel: "debug"
      }
    }
  }
  
};