const state = {
    list: undefined,
    current: undefined
}

const actions = {
    async GET_COURSE_DATA({commit, rootState}, courseId=null) {
        let url = '/api/v1/courses/' + courseId

        const response = await rootState.config.api_client.get(url)
        if (response.status === 200) {
            commit('SET_COURSE_DATA', response.data.result)
        }
    },
    async GET_MY_COURSES({commit, rootState}) {
        let url = '/api/v1/courses?my=my'
        const response = await rootState.config.api_client.get(url)

        if (response.status === 200) {
            commit('SET_COURSES', response.data.result)
        }
    },
    async GET_COURSES({commit, rootState}, my=null) {
        let url
        if(my === null) {
            url = '/api/v1/courses'
        } else {url = '/api/v1/courses?my=my'}
        const response = await rootState.config.api_client.get(url)

        if (response.status === 200) {
            commit('SET_COURSES', response.data.result)
        }
    }
}

const mutations = {
    SET_COURSE_DATA: (state, course) => {
        state.current = course
    },
    SET_COURSES: (state, courses) => {
        state.list = courses
    }
}

const getters = {
    COURSE_DATA(state) {
        return state.current;
    },
    COURSES(state) {
        return state.list;
    },
}


export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}