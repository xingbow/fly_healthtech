// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawComparison from './drawComparison.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'ComparisonView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'comparisonContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawComparison.layout(videoData)
        }
    },
    mounted: function () {
        this.drawComparison = new DrawComparison(this.containerId)
    }
}
