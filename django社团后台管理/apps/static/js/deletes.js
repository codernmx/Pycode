function delAll(argument) {
            var data = tableCheck.getData();
            layer.confirm('确认要删除吗？', function (index) {
                $.ajax({
                    data: {"data_s": data.join(',')},
                    dataType: "json",
                    type: "DELETE",
                    success: function (data) {
                        if (data.status === 0) {
                            layer.msg('删除成功', {icon: 1});
                            $(".layui-form-checked").not('.header').parents('tr').remove();
                        } else {
                            layer.msg('删除失败', {icon: 2});
                        }
                    }
                });
            });
        }