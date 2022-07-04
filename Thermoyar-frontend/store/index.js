import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

let store = new Vuex.Store({
    state: {
        pressures: [
            // water
            {
                compressedPressures: [500, 2000, 10000, 15000, 20000, 30000, 50000],
                superheatPressures: [10,50,100,200,300,400,600,800,1000,1200,1400,1600,1800,2000,2500,3000,4000,8000,10000,15000,20000,30000,40000]
            },
    
            // ammonia
            {
                compressedPressures: [],
                superheatPressures: [50,100,150,200,300,400,500,600,800,1000,1200,1400,1600,2000,5000,10000]
            }
        ]
    }
});

export default store;