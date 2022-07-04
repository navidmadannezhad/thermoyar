<template>
    <div class="superheat-content">
        <div class="calculator-section">

            <div class="inputs">
                <div class="temperature">
                    <p class="intro">برحسب سیلیسیوس</p>
                    <input type="text" v-model="temperature" name="temperature" placeholder=" دما رو وارد کن">
                </div>
                <div class="pressure">
                    <p class="intro">برحسب کیلو پاسکال</p>
                    <select name="wanted" v-model="pressure">
                        <option value="what" selected disabled>فشار رو انتخاب کن</option>
                        <option :value="pressure" v-for="pressure in superheatPressures" :key="pressure">{{ pressure }}</option>
                    </select>
                </div>
            </div>

            <div class="initialization">
                <select name="wanted" v-model="wanted">
                    <option value="what" selected disabled>چی رو میخوای؟</option>
                    <option value="vol">حجم مخصوص - V</option>
                    <option value="eng">انرژی داخلی  - U</option>
                    <option value="antal">آنتالپی  - H</option>
                    <option value="ant">آنتروپی  - S</option>
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
            temperature: '',
            pressure: 'what',
            wanted: 'what',
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
                    material: parseInt(this.material, 10)
                }
                axios.post('http://thermoyar.ir/api/v1/superheat/', data).then( res => {
                    this.loading = false;
                    this.result = res.data
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

        selectedMaterial(){
            return this.$parent.selectedMaterial;
        },

        superheatPressures(){
            return this.$store.state.pressures[this.selectedMaterial-1].superheatPressures;
        }
    },

    mounted(){

    }
}
</script>

<style lang="scss" scoped>
div.superheat-content{
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
                select{
                    margin-top: 10px;
                    width: 100%;
                    padding: 5px;
                    border-radius: 5px;
                    color: black;
                    font-size: 0.8rem;
                    option{
                        color: black !important;
                    }
                    option[value="what"]{
                        color: #6d6d6d;
                    }
                }
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
                color: black;
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
                text-align: center;
                color: #FF373E;
            }
        }
    }
}

@media only screen and (min-width: 1000px){
    div.superheat-content{
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
                    select{
                        width: 50%;
                        option[value="what"]{
                            color: #6d6d6d;
                        }
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