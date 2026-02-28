import sqlite3
import os
from typing import Dict, Optional, Any, List

class PetAIDB:
    """AI桌宠设定数据库（纯文本，无图片）"""

    def __init__(self, db_path="app/utils/DB/pet_ai.db"):
        self.db_path = db_path
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
        self._init_table()

    def _get_connection(self):
        """获取数据库连接，自动启用外键约束"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _init_table(self):
        """初始化桌宠表"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS pet_settings (
                    pet_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 宠物ID
                    pet_name TEXT NOT NULL,-- 宠物名称
                    pet_worldview TEXT,    -- 世界观背景
                    pet_personality TEXT,  -- 性格
                    pet_speech_style TEXT, -- 说话方式
                    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                ''')
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS pet_lines (
                    line_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pet_id INTEGER NOT NULL,
                    line_content TEXT NOT NULL,
                    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (pet_id) REFERENCES pet_settings(pet_id) ON DELETE CASCADE
                )
                ''')
        except sqlite3.Error as e:
            print("初始化表失败:", e)
    # ==================== 宠物增删改查 ====================
    def add_pet(self,
                pet_name: str,
                pet_worldview: str = "",
                pet_personality: str = "",
                pet_speech_style: str = "") -> Optional[int]:
        """添加桌宠设定"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO pet_settings
                (pet_name, pet_worldview, pet_personality, pet_speech_style)
                VALUES (?, ?, ?, ?)
                ''', (pet_name, pet_worldview, pet_personality, pet_speech_style))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print("添加失败:", e)
            return None

    def get_pet(self, pet_id: int = None, pet_name: str = None) -> Optional[Dict[str, Any]]:
        """按ID或名称查询单个桌宠"""
        if not pet_id and not pet_name:
            return None

        try:
            with self._get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                if pet_id:
                    cursor.execute("SELECT * FROM pet_settings WHERE pet_id = ?", (pet_id,))
                else:
                    cursor.execute("SELECT * FROM pet_settings WHERE pet_name = ?", (pet_name,))
                row = cursor.fetchone()
                return dict(row) if row else None
        except sqlite3.Error as e:
            print("查询失败:", e)
            return None

    def get_all_pets(self) -> list[Dict[str, Any]]:
        """查询所有桌宠"""
        try:
            with self._get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM pet_settings ORDER BY pet_id ASC")
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print("查询全部失败:", e)
            return []

    def update_pet(self, pet_id: int, **kwargs) -> bool:
        """
        更新桌宠，支持任意字段组合
        示例：update_pet(1, pet_name="小夜", pet_personality="高冷")
        """
        valid_fields = ["pet_name", "pet_worldview", "pet_personality", "pet_speech_style"]
        update_fields = [k for k in kwargs if k in valid_fields]

        if not update_fields:
            return False

        set_clause = ", ".join(f"{f} = ?" for f in update_fields)
        values = [kwargs[f] for f in update_fields] + [pet_id]

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"UPDATE pet_settings SET {set_clause} WHERE pet_id = ?", values)
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("更新失败:", e)
            return False

    def delete_pet(self, pet_id: int) -> bool:
        """删除桌宠"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM pet_settings WHERE pet_id = ?", (pet_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("删除失败:", e)
            return False
    # ==================== 台词增删改查 ====================
    def add_line(self, pet_id: int, line_content: str) -> Optional[int]:
        """添加桌宠台词"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO pet_lines
                (pet_id, line_content)
                VALUES (?, ?)
                ''', (pet_id, line_content))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print("添加台词失败:", e)
            return None
    def get_lines(self, pet_id: int) -> List[Dict[str, Any]]:
        """获取这个宠物的所有台词"""
        try:
            with self._get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('''
                SELECT * FROM pet_lines WHERE pet_id = ?
                ''', (pet_id,))
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print("获取台词失败:", e)
            return []
    def update_line(self, line_id: int, new_content: str) -> bool:
        """修改某一句台词"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE pet_lines
                SET line_content = ?
                WHERE line_id = ?
                ''', (new_content, line_id))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("更新台词失败:", e)
            return False
    def delete_line(self, line_id: int) -> bool:
        """删除某一句台词"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM pet_lines WHERE line_id = ?", (line_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("删除台词失败:", e)
            return False


    def get_pet_with_lines(self, pet_id: int) -> Optional[Dict[str, Any]]:
        """一次性拿到：宠物信息 + 全部台词"""
        pet = self.get_pet(pet_id=pet_id)
        if not pet:
            return None
        pet["lines"] = self.get_lines(pet_id)
        return pet


if __name__ == '__main__':
    db = PetAIDB()

    # # 1. 添加宠物
    # pet_id = db.add_pet(
    #     pet_name="小夜",
    #     pet_worldview="来自夜晚的精灵",
    #     pet_personality="高冷",
    #     pet_speech_style="简短、冷淡"
    # )

    # # 2. 给宠物加台词
    # db.add_line(pet_id, "你来了。")
    # db.add_line(pet_id, "……")
    # db.add_line(pet_id, "别烦我。")

    # # 3. 获取全部台词
    # lines = db.get_lines(pet_id)
    # for line in lines:
    #     print(line["line_content"])

    # # 4. 拿到宠物+所有台词
    # pet = db.get_pet_with_lines(pet_id)
    # print(pet)

    # 4. 删除
    # db.delete_pet(2)