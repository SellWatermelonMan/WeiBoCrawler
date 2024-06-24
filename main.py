import os
import pandas as pd
from rich.progress import track
from get_main_body import get_all_main_body
from get_comments_level_one import get_all_level_one
from get_comments_level_two import get_all_level_two
import logging

logging.basicConfig(level=logging.INFO)


class WBParser:
    def __init__(self, cookie):
        self.cookie = cookie

        os.makedirs("./WBData", exist_ok=True)
        os.makedirs("./WBData/Comments_level_1", exist_ok=True)
        os.makedirs("./WBData/Comments_level_2", exist_ok=True)
        self.main_body_filepath = "./WBData/demo.csv"
        self.comments_level_1_filename = "./WBData/demo_comments_one.csv"
        self.comments_level_2_filename = "./WBData/demo_comments_two.csv"
        self.comments_level_1_dirpath = "./WBData/Comments_level_1/"
        self.comments_level_2_dirpath = "./WBData/Comments_level_2/"

    def get_main_body(self, q, kind):
        data = get_all_main_body(self.q, self.kind, self.cookie)
        data = data.reset_index(drop=True).astype(str).drop_duplicates()
        data.to_csv(self.main_body_filepath, encoding="utf_8_sig")

    def get_comments_level_one(self):
        data_list = []
        main_body = pd.read_csv(self.main_body_filepath, index_col=0)

        logging.info(f"主体内容一共有{main_body.shape[0]:5d}个，现在开始解析...")

        for ix in track(range(main_body.shape[0]), description=f"解析中..."):
            uid = main_body.iloc[ix]["uid"]
            mid = main_body.iloc[ix]["mid"]
            final_file_path = f"{self.comments_level_1_dirpath}{uid}_{mid}.csv"

            if os.path.exists(final_file_path):
                length = pd.read_csv(final_file_path).shape[0]
                if length > 0:
                    continue

            data = get_all_level_one(uid=uid, mid=mid, cookie=self.cookie)
            data.drop_duplicates(inplace=True)
            data.to_csv(final_file_path, encoding="utf_8_sig")
            data_list.append(data)
        logging.info(f"主体内容一共有{main_body.shape[0]:5d}个，已经解析完毕！")
        data = pd.concat(data_list).reset_index(drop=True).astype(str).drop_duplicates()
        data.to_csv(self.comments_level_1_filename)

    def get_comments_level_two(self):
        data_list = []
        comments_level_1_data = pd.read_csv(self.comments_level_1_filename, index_col=0)

        logging.info(
            f"一级评论一共有{comments_level_1_data.shape[0]:5d}个，现在开始解析..."
        )

        for ix in track(
            range(comments_level_1_data.shape[0]), description=f"解析中..."
        ):
            main_body_uid = comments_level_1_data.iloc[ix]["main_body_uid"]
            mid = comments_level_1_data.iloc[ix]["mid"]
            final_file_path = (
                f"{self.comments_level_2_dirpath}{main_body_uid}_{mid}.csv"
            )

            if os.path.exists(final_file_path):
                length = pd.read_csv(final_file_path).shape[0]
                if length > 0:
                    continue

            data = get_all_level_two(uid=main_body_uid, mid=mid, cookie=self.cookie)
            data.drop_duplicates(inplace=True)
            data.to_csv(final_file_path, encoding="utf_8_sig")
            data_list.append(data)
        logging.info(
            f"一级评论一共有{comments_level_1_data.shape[0]:5d}个，已经解析完毕！"
        )
        data = pd.concat(data_list).reset_index(drop=True).astype(str).drop_duplicates()
        data.to_csv(self.comments_level_2_filename)


if __name__ == "__main__":
    q = "#姜萍中考621分却上中专的原因#"  # 话题
    kind = "综合"  # 综合，实时，热门，高级
    cookie = "SINAGLOBAL=8518412904158.368.1713933172488; SUB=_2A25La68FDeRhGeFJ4lIT9CzNyj6IHXVoCK7NrDV8PUNbmtANLXetkW9NfsmQ4Qz8zDr0mXZfri_ta_ZUdx1oaRtm; ALF=02_1721199701; _s_tentry=www.weibo.com; Apache=2102778680934.707.1718678424260; XSRF-TOKEN=PRz0XbyfMJG4mq7eMDRnCAPT; ULV=1718678424414:3:2:2:2102778680934.707.1718678424260:1718607749265; WBPSESS=2bPq4LTfaY-EnTnt8h5hWX9KGoz50scMNqd4lpDCT8IiCLnpv2C9Z_Kk8JVbYkIyBQ0eFNYccRFpnV_A6ntYbzFhGRa6K_Y0y_9c3zhS6S73tx-mc1RjJ-zr1RH9K8LXJeEA0KnwBx7zuzsiTaBcug=="
    wbparser = WBParser(cookie)
    wbparser.get_main_body(q, kind)
    # wbparser.get_comments_level_two()
