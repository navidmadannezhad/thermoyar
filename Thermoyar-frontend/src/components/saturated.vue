<template>
    <div class="saturated-content">
        <div class="calculator-section">

            <div class="inputs">
                <div class="pressure">
                    <p class="intro">برحسب کیلو پاسکال</p>
                    <input type="text" name="pressure" placeholder="یا فشار رو وارد کن" v-model="pressure">
                </div>
                <div class="temperature">
                    <p class="intro">برحسب سیلیسیوس</p>
                    <input type="text" name="temperature" placeholder="یا دما رو وارد کن" v-model="temperature">
                </div>
            </div>

            <div class="initialization">
                <select name="wanted" v-model="wanted">
                    <option value="what" selected disabled>چی رو میخوای؟</option>
                    <option value="temp" v-if="pressure && !temperature">دمای متناسب T</option>
                    <option value="pres" v-if="temperature && !pressure">فشار متناسب P</option>
                    <option value="vol_f">حجم سیال - Vf</option>
                    <option value="vol_g">حجم گاز - Vg</option>
                    <option value="vol_fg">حجم سیال گاز - Vfg</option>
                    <option value="eng_f">انرژی داخلی سیال - Uf</option>
                    <option value="eng_g">انرژی داخلی گاز - Ug</option>
                    <option value="eng_fg">انرژی داخلی سیال گاز - Ufg</option>
                    <option value="antal_fe">آنتالپی سیال - Hf</option>
                    <option value="antal_g">آنتالپی گاز - Hg</option>
                    <option value="antal_fg">آنتالپی سیال گاز - Hfg</option>
                    <option value="ant_f">آنتروپی سیال - Sf</option>
                    <option value="ant_g">آنتروپی گاز - Sg</option>
                    <option value="ant_fg">آنتروپی سیال گاز - Sfg</option>
                </select>
                <button v-on:click="calculate">محاسبه</button>
            </div>

        </div>

        <div class="results-section">
            <p class="intro">نتیجه:</p>
            <div class="result-container">
                <transition name="result-transition" mode="out-in">
                <div key=1 class="loader" v-if="loading">
                    <p>واسا تا بگردم</p>
                    <ring-loader :color="spinnerColor"></ring-loader>
                </div>
                <div key=2 ref="result" class="result" v-else>{{ result }}</div>
                </transition>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    props: [
        'material'
    ],
    data: function(){
        return{
            loading: false,
            windowWidth: window.innerWidth,
            wanted: 'what',
            pressure: '',
            temperature: '',
            result: ' - '
        }
    },
    methods:{
        calculate: function(){
            let self = this;
            if(this.robotIsNotInPage()){
                this.scrollToResult();
                this.loading = true;
                let data = {
                    wanted: this.wanted,
                    pressure: this.pressure,
                    temperature: this.temperature,
                    material: parseInt(this.selectedMaterial, 10)
                }
                axios.post('http://thermoyar.ir/api/v1/saturate/', data).then( res => {
                    this.loading = false;
                    this.result = res.data
                    console.log(res.data)
                }).catch( err => {
                    this.loading = false;
                    if(!err.response){
                        self.result = 'مشکل در برقراری ارتباط با سرور';
                    }else{
                        self.result = 'مشکل در سرور :(';
                    }
                });
            }
        },
        scrollToResult: function(){
            let weAreInPhone = this.windowWidth < 1000;
            if(weAreInPhone)
            this.$refs.result.scrollIntoView({ 
                behavior: 'smooth' 
            });
        },
        robotIsNotInPage: function(){
            if(this.$parent.emailInput || this.$parent.nameInput || this.thermoyarInput || this.$parent.phoneInput){
                return false;
            }else{
                return true;
            }
        }
    },
    computed:{
        spinnerColor: function(){
            return "#ff373e";
        },
        selectedMaterial: function(){
            return this.material == undefined ? "1" : this.material;
        }
    },
    mounted(){

    }
}
</script>

<style lang="scss" scoped>
div.saturated-content{
    width:80%;
    div.calculator-section{
        width: 100%;
        div.inputs{
            display: flex;
            justify-content: space-between;
            p{
                margin: 0px;
                color: #6d6d6d;
                font-size: 0.8rem;
            }
            p.or{
                margin-top: 20px;
            }
            div{
                margin-top: 20px;
                width: 45%;
                align-items: center;
                display: flex;
                flex-direction: column;
                input{
                    width: 100%;
                    margin-top: 10px;
                    color: black;
                    border: none;
                    border-radius: 5px;
                    padding: 5px;
                }
                input::placeholder{
                    color: #6d6d6d;
                    font-size: 0.8rem;
                }
            }
        }
        div.initialization{
            width: 100%;
            margin-top: 20px;
            display: flex;
            justify-content: space-between;
            select{
                width: 50%;
                padding: 5px;
                border-radius: 5px;
                color: black !important;
                font-size: 0.8rem;
                option{
                    color: black !important;
                }
            }
            button{
                border: none;
                background-color: #FF373E;
                padding: 10px 25px;
                border-radius: 5px;
                font-size: 0.8rem;
            }
        }
    }

    div.results-section{
        margin-top: 20px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        p.intro{
            color: #6d6d6d;
        }
        div.result-container{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;
            div.loader{
                display: flex;
                align-items: center;
                p{
                    padding: 0px 5px;
                    font-size: 0.8rem;
                    color: #FF373E;
                    margin: 0px;
                }
            }
            div.result{
                font-size: 2rem;
                color: #FF373E;
                text-align: center;
            }
        }
    }
}

@media only screen and (min-width: 1000px){
    div.saturated-content{
        display: flex;
        justify-content: space-between;
        margin-top: 50px;
        div.calculator-section{
            div.inputs{
                flex-direction: column;
                align-items: flex-start;
                p.or{
                    margin-top: 20px;
                }
                div{
                    width: 70%;
                    justify-content: space-between;
                    flex-direction: row-reverse;
                    input{
                        width: 50%;
                        margin-top: 10px;
                    }
                }
            }
            div.initialization{
                width: 70%;
                margin-top: 30px;
            }
        }

        div.results-section{
            margin-top: 20px;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            p.intro{
                color: #6d6d6d;
            }
            div.result-container{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 200px;
            }
        }
    }
}

/* animations -- */
@keyframes fade{
    from{
        opacity: 0.5;
    }
    to{
        opacity: 1;
    }
}
</style>