// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawDatabase from './drawDatabase.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'DatabaseView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'databaseContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawDatabase.layout(videoData)
        }
    },
    mounted: function () {
        this.drawDatabse = new DrawDatabase(this.containerId)
    }
}
