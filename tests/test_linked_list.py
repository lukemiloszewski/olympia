from typing import Any, List, Optional

import pytest

from olympia.linked_list import LinkedList, Node


class TestNode:
    def test_node_init(self) -> None:
        node = Node(1)

        assert isinstance(node, Node)
        assert node.data == 1
        assert node.next is None

    def test_node_repr(self) -> None:
        node = Node(1)

        assert repr(node) == "1"


class TestLinkedList:
    @classmethod
    def create_linked_list(
        self, node_data: Optional[List[Any]] = None
    ) -> LinkedList:
        ll = LinkedList()

        if node_data is None:
            return ll

        node = Node(node_data.pop(0))
        ll.head = node
        for data in node_data:
            node.next = Node(data)
            node = node.next
        return ll

    def test_linked_list_init(self) -> None:
        ll = self.create_linked_list()

        assert isinstance(ll, LinkedList)
        assert repr(ll) == "None"
        assert ll.head is None

    def test_linked_list_repr(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        assert repr(ll) == "1 -> 2 -> 3 -> None"

    def test_add_first(self) -> None:
        ll = self.create_linked_list([1, 2])
        ll.add_first(4)

        assert repr(ll) == "4 -> 1 -> 2 -> None"

        assert isinstance(ll.head, Node)
        assert ll.head.data == 4

    def test_add_last(self) -> None:
        ll = self.create_linked_list([1, 2])
        ll.add_last(3)

        assert repr(ll) == "1 -> 2 -> 3 -> None"

        assert isinstance(ll.head, Node)
        assert isinstance(ll.head.next, Node)
        assert isinstance(ll.head.next.next, Node)
        assert ll.head.next.next.data == 3

    def test_add_last_empty(self) -> None:
        ll = self.create_linked_list()
        ll.add_last(1)

        assert repr(ll) == "1 -> None"

        assert isinstance(ll.head, Node)
        assert ll.head.data == 1

    def test_add_before_at_head(self) -> None:
        ll = self.create_linked_list([1, 2])
        ll.add_before(3, 1)

        assert repr(ll) == "3 -> 1 -> 2 -> None"

        assert isinstance(ll.head, Node)
        assert ll.head.data == 3

    def test_add_before_not_at_head(self) -> None:
        ll = self.create_linked_list([1, 2])
        ll.add_before(3, 2)

        assert repr(ll) == "1 -> 3 -> 2 -> None"

        assert isinstance(ll.head, Node)
        assert isinstance(ll.head.next, Node)
        assert ll.head.next.data == 3

    def test_add_before_empty(self) -> None:
        ll = self.create_linked_list()

        with pytest.raises(Exception) as e:
            ll.add_before(4, 1)

        assert str(e.value) == "Linked list is empty"

    def test_add_before_data_not_found(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        with pytest.raises(Exception) as e:
            ll.add_before(4, 5)

        assert str(e.value) == "Node data not found: 5"

    def test_add_after(self) -> None:
        ll = self.create_linked_list([1, 2])
        ll.add_after(3, 1)

        assert repr(ll) == "1 -> 3 -> 2 -> None"

        assert isinstance(ll.head, Node)
        assert isinstance(ll.head.next, Node)
        assert ll.head.next.data == 3

    def test_add_after_empty(self) -> None:
        ll = self.create_linked_list()

        with pytest.raises(Exception) as e:
            ll.add_after(4, 1)

        assert str(e.value) == "Linked list is empty"

    def test_add_after_data_not_found(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        with pytest.raises(Exception) as e:
            ll.add_after(4, 5)

        assert str(e.value) == "Node data not found: 5"

    def test_remove_first_occurence_at_head(self) -> None:
        ll = self.create_linked_list([1, 2, 1])
        ll.remove_first_occurence(1)

        assert repr(ll) == "2 -> 1 -> None"

        assert isinstance(ll.head, Node)
        assert isinstance(ll.head.next, Node)
        assert ll.head.data == 2
        assert ll.head.next.data == 1
        assert ll.head.next.next is None

    def test_remove_first_occurence_not_at_head(self) -> None:
        ll = self.create_linked_list([1, 2, 1, 2])
        ll.remove_first_occurence(2)

        assert repr(ll) == "1 -> 1 -> 2 -> None"

        assert isinstance(ll.head, Node)
        assert isinstance(ll.head.next, Node)
        assert isinstance(ll.head.next.next, Node)
        assert ll.head.data == 1
        assert ll.head.next.data == 1
        assert ll.head.next.next.data == 2
        assert ll.head.next.next.next is None

    def test_remove_first_occurence_empty(self) -> None:
        ll = self.create_linked_list()

        with pytest.raises(Exception) as e:
            ll.remove_first_occurence(1)

        assert str(e.value) == "Linked list is empty"

    def test_remove_first_occurence_data_not_found(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        with pytest.raises(Exception) as e:
            ll.remove_first_occurence(4)

        assert str(e.value) == "Node data not found: 4"

    def test_clear(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        assert isinstance(ll, LinkedList)
        assert repr(ll) == "1 -> 2 -> 3 -> None"
        assert ll.head is not None

        ll.clear()

        assert isinstance(ll, LinkedList)
        assert repr(ll) == "None"
        assert ll.head is None

    def test_contains(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        assert ll.contains(1)
        assert not ll.contains(4)

    def test_size(self) -> None:
        ll = self.create_linked_list([1, 2, 3])

        assert ll.size() == 3
