#!/usr/bin/env python3
"""
AI偏见案例数据库导出脚本
任何人都可以使用此脚本导出完整数据库
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path

def export_to_json(cases, output_dir):
    """导出为JSON格式"""
    output_path = os.path.join(output_dir, "cases_export.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "exported_at": datetime.now().isoformat(),
            "total_cases": len(cases),
            "cases": cases
        }, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON导出完成: {output_path}")
    return output_path

def export_to_csv(cases, output_dir):
    """导出为CSV格式（简化版，便于分析）"""
    output_path = os.path.join(output_dir, "cases_export.csv")
    
    # 简化字段
    simplified = []
    for case in cases:
        simplified.append({
            "case_id": case.get("case_id"),
            "reported_at": case.get("reported_at"),
            "ai_name": case.get("ai_system", {}).get("name"),
            "ai_company": case.get("ai_system", {}).get("company"),
            "bias_type": case.get("bias_type"),
            "status": case.get("status"),
            "severity": case.get("impact", {}).get("severity"),
            "affected_population": case.get("impact", {}).get("affected_population"),
            "public_source": case.get("public_source"),
            "contributor": case.get("contributor", "tech-optimist")
        })
    
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        if simplified:
            writer = csv.DictWriter(f, fieldnames=simplified[0].keys())
            writer.writeheader()
            writer.writerows(simplified)
    
    print(f"✅ CSV导出完成: {output_path}")
    return output_path

def main():
    # 数据库路径
    script_dir = Path(__file__).parent
    db_path = script_dir.parent / "cases" / "cases.json"
    output_dir = script_dir.parent / "exports"
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取数据
    with open(db_path, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    
    print(f"📊 数据库包含 {len(cases)} 个案例")
    
    # 导出
    json_path = export_to_json(cases, output_dir)
    csv_path = export_to_csv(cases, output_dir)
    
    # 创建快照
    snapshot_dir = script_dir.parent / "snapshots" / datetime.now().strftime("%Y-%m-%d")
    os.makedirs(snapshot_dir, exist_ok=True)
    export_to_json(cases, snapshot_dir)
    export_to_csv(cases, snapshot_dir)
    print(f"📸 快照已保存: {snapshot_dir}")
    
    print("\n" + "="*50)
    print("导出完成！")
    print(f"JSON文件: {json_path}")
    print(f"CSV文件: {csv_path}")
    print("="*50)

if __name__ == "__main__":
    main()