<template>
  <div class="app-content">
    <div class="app-header">
            <div class="material">
              <p class="intro">ماده مورد نظرت:</p>
              <select id="materials" v-on:change="updateMaterialValueForComponents" v-model="selectedMaterial">
                <option value="1">آب</option>
                <option value="2">آمونیاک</option>
              </select>
            </div>
  
            <div class="state">
              <p class="intro">حالت ماده:</p>
              <div class="router-links" ref="routerLinks">
                <router-link ref="saturatedBtn" :to="{ name: 'saturated', params:{ material: selectedMaterial } }" style="border-radius: 0px 5px 5px 0px;">اشباع</router-link>
                <router-link ref="superHeatBtn" :to="{ name: 'superHeat', params:{ material: selectedMaterial } }">فوق داغ</router-link>
                <router-link ref="compressedBtn" :to="{ name: 'compressed', params:{ material: selectedMaterial } }" style="border-radius: 5px 0px 0px 5px;" :class="[selectedMaterial == 2 ? 'router-link-inactive' : '']">مادون سرد</router-link>
              </div>
            </div>

          </div>

          <form class="my-Form" method="post" action="#">
            <input ref="name" type="text" name="username" v-model="nameInput">
            <input ref="phone" type="number" name="phone_number" v-model="phoneInput">
            <input ref="email" type="email" name="email" v-model="emailInput">
            <input ref="thermoyar" type="text" name="thermoyar" v-model="thermoyarInput">
          </form>

          <div class="app-main">
            <div class="router-views">
              <transition name="fade" mode="out-in">
                <router-view></router-view>
              </transition>
            </div>
          </div>

  </div>
</template>



<script>
export default {
  data: function(){
    return{
      selectedMaterial: 1,
      nameInput: '',
      phoneInput: '',
      emailInput: '',
      thermoyarInput: ''
    }
  },
  methods:{
    updateMaterialValueForComponents: function(event){
      this.$router.push({name: 'saturated'});
      /* We use a MASTMALI  method to inject material into prev and next component. All we have to do is to press the next link and the current router link again! This way, the prop will be injected again in the current component*/
      setTimeout(()=>{
          let activeLinkIndex;
          let links = this.$refs.routerLinks.childNodes;

          Object.keys(links).forEach(index => {
            if(links[index].classList.contains('router-link-active')){
              activeLinkIndex = index;
            }
          });

          if(activeLinkIndex == links.length - 1){
            links[parseFloat(activeLinkIndex - 1)].click();
          }else{
            links[parseFloat(activeLinkIndex) + 1].click(); 
          }
          links[activeLinkIndex].click();
        },100);
    },
  },
  mounted(){
    this.$router.push({ name: 'saturated', params: { material: this.selectedMaterial } }).catch(()=>{

    });
  },
}
</script>



<style lang="scss">
div.app-content{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  div.app-header{
    width: 80%;
    display: flex;
    flex-wrap: wrap;
    border-bottom: 2px solid #6d6d6d;
    padding-bottom: 20px;
    div.material , div.state{
      margin-top: 20px;
      width:100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      p{
        color: #6d6d6d;
        margin-bottom: 5px;
      }
      *:not(p){
        width:80%;
      }
    }
    div.material{
      select{
        border-radius: 5px;
        width: 100%;
        color: black;
        font-size: 0.8rem;
      }
      option{
        color: black;
      }
    }
    div.state{
      div.router-links{
        display: flex;
        width: 100%;
        justify-content: space-between;
        a{
          display: inline-block;
          text-align: center;
          padding: 10px;
          color: white;
          background-color: #242424;
          font-size: 0.8rem;
        }
      }
    }
  }
  div.app-main{
    width: 100%;
    div.router-views{
      width: 100%;
      display: flex;
      justify-content: center; 
    }
  }
}


.router-link-exact-active{
  background-color: #ff373e !important;
}

.router-link-inactive{
  background-color: rgb(167, 167, 167) !important;
  pointer-events: none;
  cursor: default;
}

@media only screen and (min-width: 1000px){
div.app-content{
  width: 100%;
  display: flex;
  justify-content: center;
    div.app-header{
      width: 80%;
      display: flex;
      justify-content:space-between;
      padding-bottom: 100px;
      div.material , div.state{
        margin-top: 50px;
        width:45%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        p{
          margin: 0px;
        }
        *:not(p){
          width:80%;
        }
      }
      div.material{
        select{
          border-radius: 5px;
          color: black;
          font-size: 0.8rem;
          padding: 5px;
        }
      }
      div.state{
        div.router-links{
          display: flex;
          justify-content: space-between;
          a{
            display: inline-block;
            text-align: center;
            padding: 10px;
            color: white;
            background-color: #242424;
            font-size: 0.8rem;
          }
        }
      }
    }
  }
}

/* Router Transition -- */
.fade-enter-active, .fade-leave-active {
  transition: all 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.fade-enter-to, .fade-leave {
  opacity: 1;
}

.result-transition-enter-active, .result-transition-leave-active {
  transition: all 0.5s;
}

.result-transition-enter, .result-transition-leave-to {
  opacity: 0;
  transform: scale(0);
}

.result-transition-enter-to, .result-transition-leave {
  opacity: 1;
  transform: scale(1);
}

/* my form style */
form{
  position: absolute;
  top: 0px;
  left:0px;
  opacity: 0;
}

</style>
