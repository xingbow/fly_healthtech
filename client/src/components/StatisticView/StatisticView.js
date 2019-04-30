// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawStatistic from './drawStatistic.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'StatisticView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'statisticContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawStatistic.layout(videoData)
        }
    },
    mounted: function () {
        this.drawStatistic = new DrawStatistic(this.containerId)
    }
}
