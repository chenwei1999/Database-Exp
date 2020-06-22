<template>

  <div>
    
   <el-form :inline="true" :model="formInline" class="demo-form-inline">
  <el-form-item >
    <el-input v-model="formInline.name" placeholder="讲座名"></el-input>
  </el-form-item>
   <el-form-item >
    <el-input v-model="formInline.reporter" placeholder="汇报人"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">查询</el-button>
  </el-form-item>
</el-form>

  <el-table
    :data="tableData"
    style="width: 100%" v-loading="listLoading"
      element-loading-text="Loading">
      <el-table-column
        prop="name"
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
        prop="time"
        label="讲座时间">
      </el-table-column>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          type="primary"
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">报名</el-button>
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
import { getToken } from '../../utils/auth'
  export default {
    data() {
      return {
        tableData: [
          ],
         formInline: {
          name: '',
          reporter: ''
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
              url:'http://47.102.215.88:5001/searchlecture1',
              data:{page:vm.currentPage1,option:{name:(vm.formInline.name=='')?'null':vm.formInline.name,reporter:(vm.formInline.reporter=='')?'null':vm.formInline.reporter}}
          }).then(function (response) {
               vm.tableData=response.data.list
               vm.total=response.data.count
               vm.listLoading=false;
          })
      },
      handleEdit(index, row) {
        


           this.$confirm('是否确认报名?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
              var vm=this
         
          this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/signup',
              data:{uid:getToken(),lid:row.lid}
          }).then(function (response) {
                vm.$message({
                      message: '报名成功',
                      type: 'success'
                     
                });
               
          }).catch(() => {
                this.$message({
                message: '你已经报过名',
                type: 'warning'
                  });  
          });
            
          }).catch(() => {
                this.$message({
                message: '取消报名',
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