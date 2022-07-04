const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
  lintOnSave: false,
  configureWebpack: {
      plugins: [
        new HtmlWebpackPlugin({
          filename: 'tables.html',
          template: './public/tables.html',
        }),
        new HtmlWebpackPlugin({
          filename:'index.html',
          template: './public/index.html',
        }),
      ]
  }
}
