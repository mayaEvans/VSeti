const state = {
    list: undefined
}

const actions = {
    async GET_QUESTION_DATA({commit, rootState}, lessonId = null) {
        let url = '/api/v1/questions/lesson/' + lessonId

        const response = await rootState.config.api_client.get(url)
        if (response.status === 200) {
            commit('SET_QUESTION_DATA', response.data.result)
        }
    }
}

const mutations = {
    SET_QUESTION_DATA: (state, question) => {
        state.list = question
    }
}

const getters = {
    QUESTION_DATA(state) {
        return state.list
    }
}


export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}