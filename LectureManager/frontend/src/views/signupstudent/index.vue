<template>

  <div>
    
  

  <el-table
    :data="tableData"
    style="width: 100%"
    v-loading="listLoading"
      element-loading-text="Loading">
     <el-table-column
        prop="lecturename"
        label="讲座名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="reporter"
        label="汇报人">
      </el-table-column>
      <el-table-column
        prop="location"
        label="地点">
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
          @click="handleDelete(scope.$index, scope.row)">取消报名</el-button>
      </template>
    </el-table-column>
  </el-table>
  <br/>
  </div>
</template>

<script>
import { getToken } from '../../utils/auth'
  export default {
    data() {
      return {
        tableData: [],
         listLoading:false
      }
    },created()
    {
        
        this.fetchdata()
    },
    methods: {
      fetchdata()
      {
        this.listLoading=true
        var vm=this
        this.axios({
              method:'get',
              url:'http://47.102.215.88:5001/getsignup?uid='+getToken(),
          }).then(function (response) {
                 vm.tableData=response.data,
                 vm.listLoading=false    
                });
               
        
      },
      handleDelete(index, row) {
        this.$confirm('取消报名, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
                  var vm=this
        this.axios({
              method:'get',
              url:'http://47.102.215.88:5001/delsignup?lid='+row.lid+'&uid='+getToken(),
          }).then(function (response) {
                vm.$message({
                      message: '取消成功',
                      type: 'success'
                     
                });
               vm.tableData.splice(index, 1)
               vm.fetchdata()
          })
            
          }).catch(() => {
                this.$message({
                message: '取消操作',
                type: 'warning'
                  });  
          });
      }
    }
  }
</script>