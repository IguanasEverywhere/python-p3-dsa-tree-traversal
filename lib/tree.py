class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)

      if node['id'] == id:
        return node
      else:
        # nodes_to_visit = (node['children'] + nodes_to_visit)
        nodes_to_visit = nodes_to_visit + node['children']

    return None





















# def depth_first_traversal(node, result = []):
#   # visit each node (add it to the list of results)
#   result.append(node['value'])
#   for child in node['children']:
#     # visit each child node
#     depth_first_traversal(child, result)

#   return result