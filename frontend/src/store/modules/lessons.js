const state = {
    list: undefined,
    current: undefined
}

const actions = {
    async GET_LESSON_DATA({commit, rootState}, lessonId=null) {
        let url = '/api/v1/lessons/' + lessonId

        const response = await rootState.config.api_client.get(url)
        if (response.status === 200) {
            commit('SET_LESSON_DATA', response.data.result)
        }
    },
    async GET_LESSONS({commit, rootState}, courseId=null) {
        let url = '/api/v1/lessons/course/' + courseId
        const response = await rootState.config.api_client.get(url)

        if (response.status === 200) {
            commit('SET_LESSONS', response.data.result)
        }
    }
}

const mutations = {
    SET_LESSON_DATA: (state, lesson) => {
        state.current = lesson
    },
    SET_LESSONS: (state, lessons) => {
        state.list = lessons
    }
}

const getters = {
    LESSON_DATA(state) {
        return state.current;
    },
    LESSONS(state) {
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