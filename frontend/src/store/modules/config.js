import axios from 'axios'
import {router} from "@/router";

const state = () => ({
    baseDomain: 'http://localhost:8000',
    api_client: undefined,
    token: undefined,
    auth_status: false,
})

const getters = {
    getData: (state) => {
        return state.data;
    },
}

const actions = {
    async createAxiosClient({commit, state}) {
        const client = axios.create({
            baseURL: state.baseDomain
        })
        client.interceptors.response.use(async function (response) {
            return response
        }, async function (error) {
            if (error.response.status === 401) {
                await router.push('/account/login')
                return Promise.reject('at_does_not_exist')
            } else {
                commit('unsetNetworkError')
                return error.response
            }
        })
        client.interceptors.request.use(async function (config) {
            if (config['url'] !== "/api/v1/users/login/") {
                let token = state.token
                if (!token) {
                    token = localStorage.getItem('token')
                    if (!token) {
                        await router.push('/account/login')
                        return Promise.reject('at_does_not_exist')
                    } else {
                        commit('setConfigVar', ['access_token', token])
                    }
                }
                config['headers']['Authorization'] = 'Bearer ' + token
            }
            return config
        }, function (error) {
            return Promise.reject(error);
        });
        commit('setConfigVar', ['api_client', client])
    },
}

const mutations = {
    setConfigVar(state, data) {
        state[data[0]] = data[1]
    },
    setToken(state, token) {
        state['token'] = token
        localStorage.setItem('token', token)
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
