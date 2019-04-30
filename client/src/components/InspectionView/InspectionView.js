// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawInspection from './drawInspection.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'InspectionView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'inspectionContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawInspection.layout(videoData)
        }
    },
    mounted: function () {
        this.drawInspection = new DrawInspection(this.containerId)
    }
}
