<template>
  <div>
  <el-form ref="form" :model="form" label-width="80px" v-loading="listLoading"
      element-loading-text="Loading">
  <el-form-item label="学号">
    <el-input v-model="form.id" :disabled="true"></el-input>
  </el-form-item>
  <el-form-item label="姓名">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="手机号">
    <el-input v-model="form.phone"></el-input>
  </el-form-item>
  <el-form-item label="年龄">
    <el-input v-model="form.age"></el-input>
  </el-form-item>
  <el-form-item label="性别">
    <el-radio-group v-model="form.sex">
      <el-radio label="男"></el-radio>
      <el-radio label="女"></el-radio>
    </el-radio-group>
</el-form-item>
    <el-form-item>
    <el-button type="primary" @click="onSubmit">立即修改</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>

  </div>
  
  
</template>

<script>
import { getToken } from '../../utils/auth';
  export default {
    data() {
      return {
        form: {
         name: '',
         id:'',
         phone:'',
         sex:'',
         age:''
        },
        listLoading:false
      }
    },
    created()
    {
        this.fetchdate()
 
    },
    methods: {
      fetchdate(){
        var vm=this
        vm.listLoading=true
        this.axios({
              method:'get',
              url:'http://47.102.215.88:5001/getalterinfo?id='+getToken(),
          }).then(function (response) {
                vm.listLoading=false,
                vm.form=response.data
                
            }); 
      },
      onSubmit() {
        this.$confirm('修改个人信息, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
              var vm=this
              this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/alteruser',
              data:vm.form
          }).then(function (response) {
                vm.$message({
                      message: '恭喜你，修改信息成功',
                      type: 'success'
                });
                this.$router.push({ path:  '/login' })
            }); 
          }).catch(() => {
            
          });
        
        
      }
    }
  }
</script>