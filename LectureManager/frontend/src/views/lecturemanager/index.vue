<template>

  <div>
    
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
  <el-form-item >
    <el-input v-model="formInline.name" placeholder="名称"></el-input>
  </el-form-item>
  <el-form-item >
    <el-input v-model="formInline.reporter" placeholder="汇报人"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">查询</el-button>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="add">新建</el-button>
  </el-form-item>
</el-form>

  <el-table
    :data="tableData"
    style="width: 100%"
    v-loading="listLoading"
      element-loading-text="Loading">

     <el-table-column
        prop="lid"
        label="讲座ID"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="名称">
      </el-table-column>
     <el-table-column
        prop="reporter"
        label="报告人"
        width="180">
      </el-table-column>
      <el-table-column
        prop="time"
        label="讲座时间">
      </el-table-column>
      <el-table-column
        prop="location"
        label="讲座地点">
      </el-table-column>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
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
  <el-dialog title="新建讲座" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="讲座名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="报告人" :label-width="formLabelWidth">
      <el-input v-model="form.reporter" auto-complete="off"></el-input>
    </el-form-item>
     <el-form-item label="讲座时间" :label-width="formLabelWidth">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
 <el-form-item label="讲座地点" :label-width="formLabelWidth">
      <el-input v-model="form.location" auto-complete="off"></el-input>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="add2">确 定</el-button>
  </div>
</el-dialog>
 <el-dialog title="修改讲座信息" :visible.sync="dialogFormVisible2">
  <el-form :model="form2">
    <el-form-item label="讲座名称" :label-width="formLabelWidth">
      <el-input v-model="form2.name" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="报告人" :label-width="formLabelWidth">
      <el-input v-model="form2.reporter" auto-complete="off"></el-input>
    </el-form-item>
     <el-form-item label="讲座时间" :label-width="formLabelWidth">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form2.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form2.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
 <el-form-item label="讲座地点" :label-width="formLabelWidth">
      <el-input v-model="form2.location" auto-complete="off"></el-input>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible2 = false">取 消</el-button>
    <el-button type="primary" @click="edit">确 定</el-button>
  </div>
</el-dialog>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [],
         formInline: {
          name: '',
          reporter: ''
        },
         currentPage1: 1,
         total:20,
         dialogFormVisible: false,
         dialogFormVisible2: false,
         form: {
          name:'',
          reporter:'',
          date1:'',
          date2:'',
          location:''
        },form2: {
          lid:'',
          name:'',
          reporter:'',
          date1:'',
          date2:'',
          location:''
        },
        formLabelWidth: '120px',
        listLoading:false
      }
    },
    created()
    {
        
        this.search()
    },
    methods: {
      search(){
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
        this.form2.lid= row.lid;
        this.form2.name= row.name;
        this.form2.reporter= row.reporter;
        this.form2.location= row.location;
        this.dialogFormVisible2=true; 
        
      },
      handleDelete(index, row) {
        this.$confirm('删除讲座, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
                  var vm=this
        this.axios({
              method:'get',
              url:'http://47.102.215.88:5001/dellecture?id='+row.lid,
          }).then(function (response) {
                vm.$message({
                      message: '删除成功',
                      type: 'success'
                     
                }),
               vm.tableData.splice(index, 1),
               vm.search();
              
          })
            
          }).catch(() => {
                this.$message({
                message: '取消删除',
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
      },
      add()
      {
           this. dialogFormVisible=true;
      },
      add2()
      {
          var vm=this
          vm.form.date1=new Date(+new Date(vm.form.date1)+8*3600*1000).toISOString().replace(/T/g,' ').replace(/\.[\d]{3}Z/,'');
          vm.form.date2=new Date(+new Date(vm.form.date2)+8*3600*1000).toISOString().replace(/T/g,' ').replace(/\.[\d]{3}Z/,'');
              this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/addlecture',
              data:vm.form
          }).then(function (response) {
                vm.$message({
                      message: '创建成功',
                      type: 'success'
                });
                vm.search(),
                vm. dialogFormVisible=false;
            }); 
          
          
      },
      edit()
      {
          
          var vm=this
          vm.form2.date1=new Date(+new Date(vm.form2.date1)+8*3600*1000).toISOString().replace(/T/g,' ').replace(/\.[\d]{3}Z/,'');
          vm.form2.date2=new Date(+new Date(vm.form2.date2)+8*3600*1000).toISOString().replace(/T/g,' ').replace(/\.[\d]{3}Z/,'');
              this.axios({
              method:'post',
              url:'http://47.102.215.88:5001/alterlecture',
              data:vm.form2
          }).then(function (response) {
                vm.$message({
                      message: '修改成功',
                      type: 'success'
                });
                vm.search(),
                vm. dialogFormVisible2=false;
            }); 
      }
    }
  }
</script>