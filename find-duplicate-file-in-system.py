class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = {}
        for path in paths:
            path_list = path.split()
            for file in path_list[1:]:
                file_name, file_content = file.split('(')
                file_dict[file_content] = file_dict.get(file_content, []) + [path_list[0] + '/' + file_name]
        return [file_dict[key] for key in file_dict if len(file_dict[key]) > 1]