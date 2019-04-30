import Vue from 'vue'

var pipeService = new Vue({
    data: {
        COLLECTION2VIDEO: 'collection_2_video',
        SELECTVIDEO: 'select_video',
    },
    methods: {
        emitCollection2Video: function (msg) {
            this.$emit(this.COLLECTION2VIDEO, msg)
        },
        onCollection2Video: function (callback) {
            this.$on(this.COLLECTION2VIDEO, function (msg) {
                callback(msg)
            })
        },
        emitSelectVideo: function (msg) {
            this.$emit(this.SELECTVIDEO, msg)
        },
        onSelectVideo: function (callback) {
            this.$on(this.SELECTVIDEO, function (msg) {
                callback(msg)
            })
        }
    }
})

export default pipeService
