const state = {
    list: undefined
}

const actions = {
    async GET_REVIEWS({commit, rootState}, courseId=null) {
        let url = '/api/v1/reviews/course/' + courseId

        const response = await rootState.config.api_client.get(url)
        if (response.status === 200) {
            commit('SET_REVIEWS', response.data.result)
        }
    }
}

const mutations = {
    SET_REVIEWS: (state, reviews) => {
        state.list = reviews
    }
}

const getters = {
    REVIEWS(state) {
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