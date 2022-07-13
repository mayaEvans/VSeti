import VueRouter from 'vue-router'
import AppWrapper from "@/pages/app/AppWrapper";
import AccountWrapper from "@/pages/account/AccountWrapper";
import Register from "@/pages/account/register/Register";
import Login from "@/pages/account/login/Login";
import CoursesCatalog from "@/pages/app/catalog/CoursesCatalog";
import CourseInformation from "@/pages/app/catalog/courseInfo/CourseInformation";
import Course from "@/pages/app/catalog/courseInfo/course/Course"
import MyCourses from "@/pages/app/myCourses/MyCourses"
import CourseComplete from "@/pages/app/catalog/courseInfo/course/courseComplete/CourseComplete"

const routes = [
    {
        path: '/app',
        components: {
            page: AppWrapper,
        },
        children: [
            {
                path: 'mycourses',
                components: {
                    content: MyCourses,
                },
                name: 'CourseListMy'
            },
            {
                path: 'catalog',
                components: {
                    content: CoursesCatalog,
                },
                name: 'CoursesList'
            },
            {
                path: 'catalog/:id',
                components: {
                    content: CourseInformation,
                }
            },
            {
                path: 'catalog/complete/:id',
                components: {
                    content: CourseComplete,
                }
            },
            {
                path: 'catalog/:idcourse/:id',
                components: {
                    content: Course,
                },
            }
        ]
    },
    {
        path: '/',
        redirect: '/account/login',
        components: {
            page: AccountWrapper,
        },
    },
    {
        path: '/account',
        redirect: '/account/login',
        components: {
            page: AccountWrapper,
        },
        children: [
            {
                path: 'login',
                components: {
                    content: Login,
                }
            },
            {
                path: 'register',
                components: {
                    content: Register,
                }
            }
        ]
    }
]

export const router = new VueRouter({
    routes,
    mode: 'history'
})

