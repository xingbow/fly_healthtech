// /* global d3 $ */
// import pipeService from '../../service/pipeService'
import DrawProfile from './drawProfile.js'
// import dataService from '../../service/dataService.js'

export default {
    name: 'ProfileView',
    components: {
    },
    props: {
        videoId: String,
        videoData: Object
    },
    data() {
        return {
            containerId: 'profileContainer'
        }
    },
    watch: {
        videoData: function (videoData) {
            this.drawProfile.layout(videoData)
        }
    },
    mounted: function () {
        this.drawProfile = new DrawProfile(this.containerId)
    }
}
