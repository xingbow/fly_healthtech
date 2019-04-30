// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawTemporal from './drawTemporal.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'TemporalView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'temporalContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawTemporal.layout(videoData)
        }
    },
    mounted: function () {
        this.drawTemporal = new DrawTemporal(this.containerId)
    }
}
