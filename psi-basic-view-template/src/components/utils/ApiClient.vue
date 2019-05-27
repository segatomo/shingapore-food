<script>
import axios from 'axios'

const baseUrl = 'http://localhost:5000'

export default {
  data () {
    return {}
  },
  find: function (path, id, callback, errorHandler) {
    let targetPath = baseUrl + path + id

    axios.get(targetPath).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  search: function (pathWithQuery, callback, errorHandler, params) {
    let targetPath = baseUrl + pathWithQuery

    axios.get(targetPath, params).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  nativeSearch: function (path, callback, errorHandler) {
    axios.get(path).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  update: function (path, params, callback, errorHandler) {
    let targetPath = baseUrl + path

    axios.put(targetPath, params).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  uploadFile: function (path, file, params, callback, errorHandler) {
    let targetPath = baseUrl + path
    let formData = new FormData()
    formData.append('picture_data', file)
    let config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }
    console.log(formData)
    console.log(params)

    axios.post(targetPath, formData, config).then((response) => {
      callback(response)
    }, (error) => {
      errorHandler(error)
    })
  },
  create: function (path, params, callback, errorHandler) {
    let targetPath = baseUrl + path
    console.log(params)
    console.log(targetPath)

    axios.post(targetPath, params, {}).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  destroy: function (path, id, callback, errorHandler) {
    let targetPath = baseUrl + path + '/' + id

    axios.delete(targetPath).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  // TODO refactor to use HTTP Methods configurations
  destroyWithPath: function (path, callback, errorHandler) {
    let targetPath = baseUrl + path

    axios.delete(targetPath).then((response) => {
      callback(response)
    }).catch(function (error) {
      errorHandler(error)
    })
  },
  uploadaccount: function (path, accountinfo, callback, errorHandler) {
    let targetPath = baseUrl + path

    axios.post(targetPath, accountinfo).then((response) => {
      callback(response)
    }, (error) => {
      errorHandler(error)
    })
  }
}
</script>
