#!/bin/bash
# AI偏见案例数据库镜像同步脚本
# 每日自动同步到GitHub

set -e

# 配置
DATABASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MIRROR_DIR="/tmp/ai-bias-database-mirror"
GITHUB_REPO="https://github.com/YOUR_USERNAME/ai-bias-database.git"  # 替换为实际仓库

echo "🔄 开始同步数据库到GitHub..."

# 1. 检查GitHub仓库是否已配置
if [ ! -d "$MIRROR_DIR/.git" ]; then
    echo "📥 首次同步，克隆仓库..."
    git clone "$GITHUB_REPO" "$MIRROR_DIR" || {
        echo "⚠️  GitHub仓库尚未创建，请先创建仓库后重试"
        echo "   创建步骤："
        echo "   1. 访问 https://github.com/new"
        echo "   2. 创建名为 'ai-bias-database' 的公开仓库"
        echo "   3. 更新本脚本中的 GITHUB_REPO 变量"
        exit 1
    }
fi

# 2. 同步文件
echo "📂 同步文件..."
rsync -av --delete \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='exports' \
    --exclude='snapshots' \
    "$DATABASE_DIR/" "$MIRROR_DIR/"

# 3. 提交更改
cd "$MIRROR_DIR"
git add -A
if git diff --staged --quiet; then
    echo "ℹ️  没有新的更改需要提交"
else
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    git commit -m "自动同步: $TIMESTAMP"
    git push origin main || git push origin master
    echo "✅ 已推送到GitHub: $TIMESTAMP"
fi

echo "🎉 同步完成！"
echo "   GitHub镜像: $GITHUB_REPO"