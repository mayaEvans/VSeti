import Vue from 'vue';
import Vuex from 'vuex';
import config from '@/store/modules/config';
import courses from "@/store/modules/courses";
import lessons from "@/store/modules/lessons";
import reviews from "@/store/modules/reviews";
import certificates from "@/store/modules/certificates";
import question from "@/store/modules/question";

Vue.use(Vuex)

export const store = new Vuex.Store({
    modules: {
        config,
        courses,
        lessons,
        reviews,
        certificates,
        question
    }
})
