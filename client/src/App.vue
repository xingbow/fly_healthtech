<template>
  <div id="app" style="width: 1400px">
      <nav class="navbar sticky-top navbar-dark bg-dark" style="padding-top: 1px; padding-bottom: 1px; margin-bottom: 1px;">
          <div style="margin-top:5px; margin-left: 5px;">
              <span style="color:white; font-size:1.25rem; font-weight:500; user-select: none">FLY healthtech</span>
          </div>
      </nav>
      <!-- <div class="container-fluid" style="padding-left: 5px; padding-right: 5px"> -->
      <div class="container-fluid">
          <!-- <div class="row" style="margin-left: 10px; margin-right: 10px"> -->
            <div class="row" style="padding-left: 2px; padding-right: 2px; padding-top: 2px; padding-bottom: 2px;">
              <!-- <div class="col-6 content" style="padding-left: 3px; padding-right: 3px"> -->
              <div class="col-4 content" style="padding-left: 2px; padding-right: 2px; padding-top: 2px; padding-bottom: 2px;">
                <ProfileView :videoList="videoList" :videoId="videoId" :videoData="videoData"></ProfileView>
                <DatabaseView :videoId="videoId" :videoData="videoData"></DatabaseView>
              </div>
              <div class="col-4 content" style="padding-left: 2px; padding-right: 2px; padding-top: 2px; padding-bottom: 2px;">
                <InspectionView :videoId="videoId" :videoData="videoData"></InspectionView>
                <TemporalView :videoId="videoId" :videoData="videoData"></TemporalView>
              </div>
              <div class="col-4 content" style="padding-left: 2px; padding-right: 2px; padding-top: 2px; padding-bottom: 2px;">
                <StatisticView :videoId="videoId" :videoData="videoData"></StatisticView>
                <ComparisonView :videoId="videoId" :videoData="videoData"></ComparisonView>
              </div>
          </div>
      </div>          
  </div>
</template>

<script>
import dataService from './service/dataService'
/* global d3 $ _ */

import ProfileView from './components/ProfileView/ProfileView.vue'
import DatabaseView from './components/DatabaseView/DatabaseView.vue'
import InspectionView from './components/InspectionView/InspectionView.vue'
import TemporalView from './components/TemporalView/TemporalView.vue'
import StatisticView from './components/StatisticView/StatisticView.vue'
import ComparisonView from './components/ComparisonView/ComparisonView.vue'


export default {
  name: 'app',
  components: {
    ProfileView,
    DatabaseView,
    InspectionView,
    TemporalView,
    StatisticView,
    ComparisonView
  },
  data() {
    return {
        videoList: [],
        videoId: '',
        videoData: {}
    }
  },
  mounted: function () {
    console.log('d3: ', d3) /* eslint-disable-line */
    console.log('$: ', $) /* eslint-disable-line */
    console.log('_', _.partition([1, 2, 3, 4], n => n % 2)) /* eslint-disable-line */

    this.$nextTick(() => {
      dataService.initialization('videoId', (data) => {
        console.log('testing: ', data['data']) /* eslint-disable-line */
      })
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  margin: 0 auto;
}

.container {
  width: 100%;
  padding: 5px 5px 5px 5px;
}

.content {
  padding: 2px 2px 2px 2px;
}

footer {
  margin-left: 5px;
}
</style>
