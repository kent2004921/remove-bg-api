# Remove Background API

## 项目简介
这是一个基于 Flask 的 API，用于处理图片，包括：
- 移除图片背景。
- 裁切图片中的人脸。

## 部署方式
1. 将代码推送到 GitHub。
2. 登录 [Render](https://render.com/)。
3. 创建新服务，选择 Web Service。
4. Render 会自动检测 `render.yaml` 并完成部署。
5. 部署完成后，访问生成的 URL 测试 API。

## API 路由
### 1. 测试路由
- **URL**: `/test`
- **方法**: `GET`
- **功能**: 测试 API 是否正常工作。
- **返回**:
  ```json
  {"message": "API is working!"}
