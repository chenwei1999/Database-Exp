<template>

  <div>
    
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
  <el-form-item >
    <el-input v-model="formInline.userid" placeholder="学号"></el-input>
  </el-form-item>
  <el-form-item >
    <el-input v-model="formInline.username" placeholder="姓名"></el-input>
  </el-form-item>
  <el-form-item >
    <el-input v-model="formInline.lecturename" placeholder="讲座名"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">查询</el-button>
  </el-form-item>
</el-form>

  <el-table
    :data="tableData"
    style="width: 100%"
    v-loading="listLoading"
      element-loading-text="Loading">
     <el-table-column
        prop="userid"
        label="学号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="username"
        label="学生">
      </el-table-column>
     <el-table-column
        prop="lecturename"
        label="讲座名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="lecturetime"
        label="讲座时间">
      </el-table-column>
       <el-table-column
        prop="signuptime"
        label="报名时间">
      </el-table-column>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <br/>
   <div class="block" >
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage1"
      :page-size="15"
      layout="total, prev, pager, next"
      :total="total">
    </el-pagination>
  </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [],
         formInline: {
          userid: '',
          username: '',
          lecturename:''
        },
         currentPage1: 1,
         total:20,
         listLoading:false
      }
    },
    created()
    {
          this.search()
    },
    methods: {
      search()
      {
          this.listLoading=true
          var vm=this
          this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/searchsignup',
              data:{page:vm.currentPage1,option:{userid:(vm.formInline.userid=='')?'null':vm.formInline.userid,username:(vm.formInline.username=='')?'null':vm.formInline.username,lecturename:(vm.formInline.lecturename=='')?'null':vm.formInline.lecturename}}
          }).then(function (response) {
               vm.tableData=response.data.list,
               vm.total=response.data.count,
               vm.listLoading=false;
          })
      },
      handleDelete(index, row) {
           this.$confirm('删除该学生报名, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
                  var vm=this
        this.axios({
              method:'get',
              url:'http://47.102.215.88:5001/delsignup?lid='+row.lid+'&uid='+row.userid,
          }).then(function (response) {
                vm.$message({
                      message: '删除成功',
                      type: 'success'
                     
                });
               vm.tableData.splice(index, 1);
               vm.search()
          })
            
          }).catch(() => {
                this.$message({
                message: '取消操作',
                type: 'warning'
                  });  
          });
      },
      onSubmit() {
        this.search()
      },
       handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        this.search()
      }
    }
  }
</script>