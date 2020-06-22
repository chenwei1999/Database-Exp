import request from '@/utils/request'

export function login(data) {
  return request({
    url: 'http://47.102.215.88:5001/gettoken',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: 'http://47.102.215.88:5001/getuserinfo',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
