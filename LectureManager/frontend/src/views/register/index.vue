<template>
    <div class="content" >
    
       <div id="register-container">
            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <h3 style="margin:0px 0px 20px 200px ">用户注册</h3>
                
                 <el-form-item label="学号" prop="userid">

                    <el-input v-model.number="ruleForm.userid"></el-input>
                    </el-form-item>
   <el-form-item label="姓名" prop="username">
    <el-input v-model.number="ruleForm.username"></el-input>
  </el-form-item>

    <el-form-item label="性别" prop="sex">
    <el-select v-model="ruleForm.sex" placeholder="请选择性别">
      <el-option label="男" value="男"></el-option>
      <el-option label="女" value="女"></el-option>
    </el-select>
  </el-form-item>
     <el-form-item label="手机号" prop="phone">
    <el-input v-model.number="ruleForm.phone"></el-input>
  </el-form-item>
  <el-form-item label="年龄" prop="age">
    <el-input v-model.number="ruleForm.age"></el-input>
  </el-form-item>
    <el-form-item label="密码" prop="pass">
    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
    <el-button type="info" style="margin-left:100px" @click="back">返回</el-button>
  </el-form-item>
</el-form>
        </div>

        
        
    </div>
    
</template>

<script>
  export default {
    data() {
     
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        ruleForm: {
          userid:'',
          pass: '',
          checkPass: '',
          age: '',
          username:'',
         sex:'',
         phone:''
        },
        rules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ]
          
        }
      };
    },created()
    {
        this.$root.reload()
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            
                 this.$confirm('确定注册?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
              var vm=this
              this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/register',
              data:{userid:vm.ruleForm.userid,username :vm.ruleForm.username,password:vm.ruleForm.pass,phone :vm.ruleForm.phone,age: vm.ruleForm.age,sex :vm.ruleForm.sex}
          }).then(function (response) {
                vm.$message({
                      message: '注册成功',
                      type: 'success'
                });
                vm.$router.push({ path: '/login' })
            }).catch(()=>{
                 vm.$message({
                      message: '此用户存在',
                      type: 'warning'
                });
            }); 
          }).catch(() => {
              vm.$message({
                      message: '取消注册',
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
      },
      back()
      {
          this.$router.push({ path: '/login' })
      }
    }
  }
</script>

<style  scoped>
  .content{
    background-image: url(../../assets/TVYTbAXWheQpRcWDaDMu.svg);
    background-repeat: no-repeat;
    background-position: center 110px;
    background-size: 100%;
    width: 100%;
    height: 100%;
    
  }
  #register-container {
    position: relative;
    top: 100px;
    border-radius: 5px;
    background-clip: padding-box;
    margin: 0 auto 0;
    width: 500px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    
  }
  
</style>
