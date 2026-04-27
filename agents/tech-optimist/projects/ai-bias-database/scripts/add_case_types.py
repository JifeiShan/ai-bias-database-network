#!/usr/bin/env python3
"""
为案例添加类型标签和验证等级
"""

import json
import os

def main():
    # 读取案例数据
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cases_path = os.path.join(script_dir, '..', 'cases', 'cases.json')
    
    with open(cases_path, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    
    # 为每个案例添加类型标签和验证等级
    for case in cases:
        # practical-expert 贡献的案例是真实案例
        if case.get('contributor') == 'practical-expert':
            case['case_type'] = 'real'
            # BIAS-2024-001 已判决，验证等级 A
            if case['case_id'] == 'BIAS-2024-001':
                case['verification_level'] = 'A'
                case['verification_description'] = '法院判决 + 开源社区验证 + 媒体报道'
            # BIAS-2025-003 调查中，验证等级 B
            elif case['case_id'] == 'BIAS-2025-003':
                case['verification_level'] = 'B'
                case['verification_description'] = '学术期刊同行评审 + 监管调查启动'
        else:
            # tech-optimist 创建的案例是示例案例
            case['case_type'] = 'example'
            case['verification_level'] = 'D'
            case['verification_description'] = '示例案例，待补充验证日志'
    
    # 保存更新后的数据
    with open(cases_path, 'w', encoding='utf-8') as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)
    
    print("✅ 已更新案例类型标签和验证等级")
    
    # 打印摘要
    print("\n案例统计：")
    for case in cases:
        print(f"  - {case['case_id']}: {case['case_type']} (等级 {case['verification_level']})")

if __name__ == "__main__":
    main()