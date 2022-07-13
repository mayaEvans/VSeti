const state = {
    list: undefined
}

const actions = {
    async GET_CERT({commit, rootState}) {
        let url = '/api/v1/certificates'
        const response = await rootState.config.api_client.get(url)
        if (response.status === 200) {
            commit('SET_CERT', response.data.result)
        }
    }
}

const mutations = {
    SET_CERT: (state, certificates) => {
        state.list = certificates
    }
}

const getters = {
    CERT(state) {
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