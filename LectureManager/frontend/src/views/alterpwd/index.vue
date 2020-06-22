<template>
<div>

  <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm" >
    <div  margin-bottom="200px">  </div>
  <el-form-item label="密码" prop="pass" margin-top="200px">
      <el-col :span="12">
<el-input type="password" v-model="ruleForm2.pass" auto-complete="off" ></el-input>
      </el-col>
    
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
      <el-col :span="12">
          <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
   </el-col>
    
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm2')">提交</el-button>
    <el-button @click="resetForm('ruleForm2')">重置</el-button>
  </el-form-item>
</el-form>

</div>
  
</template>

<script>
import { getToken } from '../../utils/auth';
  export default {
    data() {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm2.checkPass !== '') {
            this.$refs.ruleForm2.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm2.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      
      return {
        ruleForm2: {
          pass: '',
          checkPass: '',
          dialogVisible:false
        },
        rules2: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
     
      
      
      
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
             this.$confirm('修改密码, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
              var token=getToken()
              var vm=this
              this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/alterpasswd',
              data:{id:token,pwd:this.ruleForm2.pass}
          }).then(function (response) {
                vm.$message({
                      message: '恭喜你，修改密码成功',
                      type: 'success'
                });
            }); 
            
          }).catch(() => {
                this.$message({
                message: '修改失败',
                type: 'warning'
                  });  
          });
            
            
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>
