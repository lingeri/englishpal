# Lab 3 : Persistence Ignorance

> 201931990124 刘长优
>
> 201931990122 黄凯峰
>
> 201931990130 王晨航
>
> 201931990127 骆纪元

## Abstract

通过对项目进行重构，理解Repository Pattern和Service Layer Pattern，以及认识分离业务层和持久层的重要性。

## Introduction

In this lab, we are going to use a non-database strategy while implementing the Repository Pattern. More specifically, we will define a repository class called PickleRepository. As the class name indicates, this class will use a pickle file as the infrastructure.

## Materials and Methods

- 利用Pickle实现PickleRepository类
- 利用Pytest测试test_services.py获得实验结果

## Results

- [updated repository.py](https://englishpal-78.readthedocs.io/en/latest/_static/repository.py)

- output we got from running pytest test services.py

	```sh
	============================= test session starts =============================
	platform win32 -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
	rootdir: D:\Project\code
	plugins: anyio-2.2.0
	collected 3 items
	
	test_services.py ...                                                     [100%]
	
	============================== warnings summary ===============================
	F:\anaconda3\lib\site-packages\pyreadline\py3k_compat.py:8
	  F:\anaconda3\lib\site-packages\pyreadline\py3k_compat.py:8: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.10 it will stop working
	    return isinstance(x, collections.Callable)
	
	-- Docs: https://docs.pytest.org/en/stable/warnings.html
	======================== 3 passed, 1 warning in 0.05s =========================
	```

- [10-second demo video for the above integration test](https://www.bilibili.com/video/BV1kv4y137Kk?spm_id_from=333.999.list.card_archive.click)

- [Read the doc](https://englishpal-78.readthedocs.io/en/latest/SA-lab3.html)

## Discussions

- What is the difference between the textbook test services.py and new test services.py?

	将FakeRepository替换为了PickleRepository

- Has the service layer been affected after we have chosen to use another implementation for the Repos-
	itory Pattern? Can we say that the service layer is ignorant of the persistence?

	当我们替换了存储层的实现时，不需要再修改服务层，测试也成功了，达成了分离它们的目的，遵守了Persistence Ignorance编码原则。

- What is the benefit of separating business logic from infrastructure concerns? Where is the business
	logic defined, and where is the infrastructure defined? Tell me the Python file name(s).

	优点：

	- 有益于重构
	- 项目耦合度低
	- 能够专心于业务，而不必同时关心持久层

​		logic: services.py

​		infrastructure: repository.py model.py