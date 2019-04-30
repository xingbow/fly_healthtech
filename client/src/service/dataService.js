import axios from 'axios'

const GET_REQUEST = 'get'
const POST_REQUEST = 'post'
const dataServerUrl = 'http://127.0.0.1:5003'

function request(url, params, type, callback) {
    let func
    if (type === GET_REQUEST) {
        func = axios.get
    } else if (type === POST_REQUEST) {
        func = axios.post
    }

    func(url, params).then((response) => {
        if (response.status === 200) {
            callback(response)
        } else {
            console.error(response) /* eslint-disable-line */
        }
    })
    .catch((error) => {
        console.error(error) /* eslint-disable-line */
    })
}

function initialization(videoId, callback) {
    const url = `${dataServerUrl}/initialization/${videoId}`
    const params = {}
    request(url, params, GET_REQUEST, callback)
}

export default {
    dataServerUrl,
    initialization
}
